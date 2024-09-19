package searcher

import (
	"bufio"
	"io/fs"
	"os"
	"path/filepath"
	"strings"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func NewGUI(path string) *GUI {
	return &GUI{path: path}
}

type GUI struct {
	path string
}

func (s *GUI) Search() ([]model.Match, error) {
	var matches []model.Match
	err := filepath.WalkDir(s.path, func(path string, d fs.DirEntry, err error) error {
		filename := d.Name()
		if !strings.HasSuffix(filename, ".py") {
			return nil
		}
		log.Debug().Msgf("raw path: %s", path)
		cleanPath := filepath.Clean(path)
		log.Debug().Msgf("Searching in path: %s", cleanPath)
		fileMatches, err := s.searchFile(cleanPath)
		if err != nil {
			return err
		}
		matches = append(matches, fileMatches...)
		return nil
	})
	return matches, err
}

func (s *GUI) searchFile(filepath string) ([]model.Match, error) {
	var err error
	pattern := viper.GetString("pattern")
	var matches []model.Match
	f, err := os.Open(filepath)
	if err != nil {
		return nil, err
	}
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if !strings.Contains(line, pattern) {
			continue
		}
		matches = append(matches, model.Match{Path: filepath, Text: line})
	}
	return matches, nil
}
