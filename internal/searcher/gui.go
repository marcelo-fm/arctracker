package searcher

import (
	"bufio"
	"io"
	"io/fs"
	"os"
	"path/filepath"
	"strings"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func NewStandard(isStdin bool, path string) *Standard {
	return &Standard{isStdin: isStdin, path: path}
}

type Standard struct {
	isStdin bool
	path    string
}

func (s *Standard) Search() ([]model.Match, error) {
	var matches []model.Match
	if s.isStdin {
		return s.search(os.Stdin, s.path)
	}
	err := filepath.WalkDir(s.path, func(path string, d fs.DirEntry, err error) error {
		filename := d.Name()
		if !strings.HasSuffix(filename, ".py") {
			return nil
		}
		log.Debug().Msgf("raw path: %s", path)
		cleanPath := filepath.Clean(path)
		log.Debug().Msgf("Searching in path: %s", cleanPath)
		f, err := os.Open(cleanPath)
		if err != nil {
			return err
		}
		fileMatches, err := s.search(f, cleanPath)
		if err != nil {
			return err
		}
		matches = append(matches, fileMatches...)
		return nil
	})
	return matches, err
}

func (s *Standard) search(reader io.Reader, filepath string) ([]model.Match, error) {
	pattern := viper.GetString("pattern")
	var matches []model.Match
	scanner := bufio.NewScanner(reader)
	for scanner.Scan() {
		line := scanner.Text()
		if !strings.Contains(line, pattern) {
			continue
		}
		matches = append(matches, model.Match{Path: filepath, Text: line})
	}
	return matches, nil
}
