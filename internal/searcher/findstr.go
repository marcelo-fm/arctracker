package searcher

import (
	"bufio"
	"bytes"
	"io"
	"io/fs"
	"os"
	"os/exec"
	"path/filepath"
	"strings"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func NewFindstr(isStdin bool, path string) *Findstr {
	cmd := exec.Command("findstr", "/?")
	err := cmd.Run()
	if err != nil {
		log.Warn().Msg("findstr is not in PATH")
		return nil
	}
	return &Findstr{isStdin: isStdin, path: path}
}

type Findstr struct {
	isStdin bool
	path    string
}

func (r *Findstr) Search() ([]model.Match, error) {
	if r.isStdin {
		return searchStdin()
	}
	var matches []model.Match
	err := filepath.WalkDir(r.path, func(path string, d fs.DirEntry, err error) error {
		filename := d.Name()
		if !strings.HasSuffix(filename, ".py") {
			return nil
		}
		log.Debug().Msgf("raw path: %s", path)
		cleanPath := filepath.Clean(path)
		log.Debug().Msgf("Searching in path: %s", cleanPath)
		fileMatches, err := searchFile(cleanPath)
		if err != nil {
			return err
		}
		matches = append(matches, fileMatches...)
		return nil
	})
	return matches, err
}

func searchFile(filepath string) ([]model.Match, error) {
	var err error
	pattern := viper.GetString("pattern")
	argsCmd1 := []string{"/n", pattern, filepath}
	log.Debug().Msgf("Searching for pattern %s in %s", pattern, filepath)
	cmd1 := exec.Command("findstr", argsCmd1...)
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
		matches[i] = model.Match{Path: filepath, Text: string(line)}
	}
	return matches, nil
}

func searchStdin() ([]model.Match, error) {
	var err error
	var reader *bufio.Reader
	pattern := viper.GetString("pattern")
	path := "Stdin"
	argsCmd1 := []string{pattern}
	reader = bufio.NewReader(os.Stdin)
	log.Debug().Msgf("Searching for pattern %s in %s", pattern, path)
	cmd1 := exec.Command("findstr", argsCmd1...)
	cmd1.Stdin = reader
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
