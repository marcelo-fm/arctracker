package searcher

import (
	"bufio"
	"bytes"
	"io"
	"os"
	"os/exec"
	"strings"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func NewGrep(isStdin bool, path string) *Grep {
	cmd := exec.Command("grep", "--version")
	err := cmd.Run()
	if err != nil {
		log.Warn().Msg("grep is not in PATH")
		return nil
	}
	return &Grep{isStdin: isStdin, path: path}
}

type Grep struct {
	isStdin bool
	path    string
}

func (r *Grep) Search() ([]model.Match, error) {
	var err error
	var reader *bufio.Reader
	pattern := viper.GetString("pattern")
	path := r.path
	argsCmd1 := []string{"-r", "--include", "'*.py'", pattern, path}
	if r.isStdin {
		path = "Stdin"
		argsCmd1 = []string{pattern}
		reader = bufio.NewReader(os.Stdin)
	}
	log.Debug().Msgf("Searching for pattern %s in %s", pattern, path)
	cmd1 := exec.Command("grep", argsCmd1...)
	if r.isStdin {
		cmd1.Stdin = reader
	}
	log.Debug().Msgf("Command 1: %s", strings.Join(cmd1.Args, " "))
	buf := new(bytes.Buffer)
	writer := bytes.NewBuffer(buf.Bytes())
	cmd1.Stdout = writer
	err = cmd1.Run()
	if err != nil {
		log.Error().Err(err).Msg("Error running command 1")
		return nil, err
	}
	out, err := io.ReadAll(writer)
	if err != nil {
		log.Error().Err(err).Msg("Error reading output")
		return nil, err
	}
	lines := bytes.Split(out, []byte("\n"))
	matches := make([]model.Match, len(lines))
	for i, line := range lines {
		arr := bytes.Split(line, []byte(":"))
		var path, text string
		if len(arr) == 1 {
			text = string(arr[0])
		} else if len(arr) >= 2 {
			path = string(arr[0])
			text = string(arr[1])
		}
		matches[i] = model.Match{Path: path, Text: text}
	}
	return matches, nil
}
