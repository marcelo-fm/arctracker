package searcher

import (
	"bytes"
	"io"
	"os/exec"
	"strings"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func NewSelectString(isStdin bool, path string) *SelectString {
	return &SelectString{isStdin: isStdin, path: path}
}

type SelectString struct {
	isStdin bool
	path    string
}

func (r *SelectString) Search() ([]model.Match, error) {
	if r.isStdin {
		srch := NewFindstr(r.isStdin, r.path)
		return srch.Search()
	}

	var err error
	pattern := viper.GetString("pattern")
	path := r.path
	argsCmd1 := []string{"-WindowStyle", "Hidden", "-Command", "Get-ChildItem", "-Path", path, "-Recurse", "|", "Select-String", "-Pattern", pattern, "-Encoding", "UTF8"}
	log.Debug().Msgf("Searching for pattern %s in %s", pattern, path)
	cmd := exec.Command("powershell", argsCmd1...)
	log.Debug().Msgf("Command 1: %s", strings.Join(cmd.Args, " "))
	buf := new(bytes.Buffer)
	writer := bytes.NewBuffer(buf.Bytes())
	cmd.Stdout = writer
	err = cmd.Run()
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
		log.Debug().Msgf("Line %d: %s", i, string(line))
		arr := bytes.Split(line, []byte(":"))
		log.Debug().Msgf("len of lineArr %d: %d", i, len(arr))
		matches[i] = model.Match{Path: string(arr[0]), Text: string(arr[len(arr)-1])}
	}
	return matches, nil
}
