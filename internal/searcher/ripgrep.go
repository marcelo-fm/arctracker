package searcher

import (
	"bufio"
	"bytes"
	"encoding/json"
	"io"
	"os"
	"os/exec"
	"strings"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func NewRipgrep(isStdin bool, path string) *Ripgrep {
	cmd := exec.Command("rg", "--version")
	err := cmd.Run()
	if err != nil {
		log.Warn().Msg("ripgrep is not in PATH")
		return nil
	}
	return &Ripgrep{isStdin: isStdin, path: path}
}

type Ripgrep struct {
	isStdin bool
	path    string
}

func (r *Ripgrep) Search() ([]model.Match, error) {
	var err error
	var reader *bufio.Reader
	pattern := viper.GetString("pattern")
	path := r.path
	argsCmd1 := []string{pattern, path, "--json", "--type=py", "--trim"}
	if r.isStdin {
		path = "Stdin"
		argsCmd1 = []string{pattern, "--json", "--trim"}
		reader = bufio.NewReader(os.Stdin)
	}
	log.Debug().Msgf("Searching for pattern %s in %s", pattern, path)
	cmd1 := exec.Command("rg", argsCmd1...)
	if r.isStdin {
		cmd1.Stdin = reader
	}
	log.Debug().Msgf("Command 1: %s", strings.Join(cmd1.Args, " "))
	cmd2 := exec.Command("jq", ".", "-sc")
	log.Debug().Msgf("Command 2: %s", strings.Join(cmd2.Args, " "))
	log.Debug().Msg("linking commands")
	cmd2.Stdin, err = cmd1.StdoutPipe()
	if err != nil {
		log.Error().Err(err).Msg("Error linking commands")
		return nil, err
	}
	buf := new(bytes.Buffer)
	writer := bytes.NewBuffer(buf.Bytes())
	cmd2.Stdout = writer
	err = cmd2.Start()
	if err != nil {
		log.Error().Err(err).Msg("Error starting command 2")
		return nil, err
	}
	err = cmd1.Run()
	if err != nil {
		log.Error().Err(err).Msg("Error running command 1")
		return nil, err
	}
	err = cmd2.Wait()
	if err != nil {
		log.Error().Err(err).Msg("Error waiting command 2")
		return nil, err
	}
	out, err := io.ReadAll(writer)
	if err != nil {
		log.Error().Err(err).Msg("Error reading output")
		return nil, err
	}
	var results []match
	err = json.Unmarshal(out, &results)
	if err != nil {
		return nil, err
	}
	matches := make([]model.Match, 0, len(results))
	for _, res := range results {
		if res.Type != "match" {
			continue
		}
		matches = append(matches, model.Match{Path: res.Data.Path.Text, Text: res.Data.Lines.Text})
	}
	return matches, nil
}

type match struct {
	Type string `json:"type"`
	Data *struct {
		Path struct {
			Text string `json:"text"`
		} `json:"path"`
		Lines struct {
			Text string `json:"text"`
		} `json:"lines"`
	} `json:"data"`
}
