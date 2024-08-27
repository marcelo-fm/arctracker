package searcher

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"os/exec"
	"strings"
	"sync"
	"unicode"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func SearchWithPath(path string, s *scraper.Scraper) ([]model.License, error) {
	pattern := viper.GetString("pattern")
	content, err := execRG(pattern, path)
	if err != nil {
		if err.Error() == "exit status 1" {
			log.Warn().Msgf("No arcpy tool found in %s", path)
			os.Exit(0)
		}
		return nil, err
	}
	return search(content, s)
}

func SearchWithStdin(reader io.Reader, s *scraper.Scraper) ([]model.License, error) {
	pattern := viper.GetString("pattern")
	var err error
	log.Debug().Msgf("Searching for pattern %s", pattern)
	cmd1 := exec.Command("rg", pattern, "--json", "--trim")
	cmd1.Stdin = reader
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
		if err.Error() == "exit status 1" {
			log.Warn().Msgf("No arcpy tool found in Stdin")
			os.Exit(0)
		}
		return nil, err
	}
	err = cmd2.Wait()
	if err != nil {
		log.Error().Err(err).Msg("Error waiting command 2")
		return nil, err
	}
	content, err := io.ReadAll(writer)
	if err != nil {
		log.Error().Err(err).Msg("Error reading output")
		return nil, err
	}
	return search(content, s)
}

func search(content []byte, s *scraper.Scraper) ([]model.License, error) {
	var err error
	baseURL := viper.GetString("baseURL")
	var contentArr []Match
	err = json.Unmarshal(content, &contentArr)
	if err != nil {
		log.Error().Err(err).Msg("Error unmarshalling content")
		return nil, err
	}
	licenses := make([]model.License, 0, len(contentArr))
	for _, content := range contentArr {
		if content.Type != "match" {
			continue
		}
		cmd := parseCommand(content)
		if cmd == "" {
			continue
		}
		url := createURL(cmd)
		if url == "" {
			continue
		}
		s.SetupLicenseScraper()
		license := s.Scrape(baseURL + url)
		if license.Title != "" && license.Name != "" {
			licenses = append(licenses, license)
		}
	}
	return licenses, nil
}

func execRG(pattern, path string) ([]byte, error) {
	var err error
	log.Debug().Msgf("Searching for pattern %s in %s", pattern, path)
	cmd1 := exec.Command("rg", pattern, path, "--json", "--type=python", "--trim")
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
	return out, nil
}

type TypeContent struct {
	Type string `json:"type"`
}

// genContent gera o chanel de bytes, que representa cada achado da palavra chave com
// regex.
func genContent(ctx context.Context, in []Match) <-chan Match {
	out := make(chan Match)
	go func() {
		defer close(out)
		for _, content := range in {
			if content.Type != "match" {
				continue
			}
			select {
			case out <- content:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func parseCommand(match Match) string {
	fullCmd := strings.Trim(match.Data.Lines.Text, " ")
	log.Debug().Msgf("Cmd of %s: %s", match.Data.Path.Text, fullCmd)
	startIndex := strings.Index(fullCmd, "arcpy.")
	if startIndex == -1 {
		return ""
	}
	log.Debug().Msgf("startIndex: %d", startIndex)
	endIndex := strings.Index(fullCmd, "(")
	if endIndex == -1 {
		return ""
	}
	if startIndex > endIndex {
		return ""
	}
	log.Debug().Msgf("endIndex: %d", endIndex)
	return fullCmd[startIndex:endIndex]
}

func parseCommandChannel(ctx context.Context, in <-chan Match) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for match := range in {
			cmd := parseCommand(match)
			select {
			case out <- cmd:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

// parseModule retorna o nome do módulo correto para a URL.
func parseModule(module string) string {
	switch module {
	case "management":
		return "data-" + module
	case "edit":
		return "editing"
	case "ddd":
		return "3d-analyst"
	default:
		return module
	}
}

// parseTool retorna o nome da ferramenta correto para a URL.
func parseTool(toolName string) string {
	switch toolName {
	case "EncloseMultiPatch":
		return "enclose-multipatch"
	}
	var tool string = strings.Clone(toolName)
	for i, r := range toolName[1:] {
		if !unicode.IsUpper(r) {
			continue
		}
		tool = tool[:i+1] + "-" + tool[i+1:]
	}
	return strings.ToLower(tool)
}

func createURL(cmd string) string {
	pattern := viper.GetString("pattern")
	if !strings.HasPrefix(cmd, pattern+".") {
		log.Warn().Msgf("%s does not start with arcpy.", cmd)
		return ""
	}
	cmdArr := strings.Split(cmd, ".")
	lastIndex := len(cmdArr) - 1
	tool := parseTool(cmdArr[lastIndex])
	var url string
	if len(cmdArr) == 3 {
		module := parseModule(cmdArr[1])
		url = fmt.Sprintf("%s/%s", module, strings.ToLower(tool))
	} else if len(cmdArr) == 2 {
		url = strings.ToLower(tool)
	}
	return url + ".htm"
}

func createURLChannel(ctx context.Context, in <-chan string) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for cmd := range in {
			url := createURL(cmd)
			if url == "" {
				continue
			}
			select {
			case out <- url:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func getLicense(ctx context.Context, s *scraper.Scraper, urls <-chan string) <-chan model.License {
	out := make(chan model.License)
	go func() {
		for url := range urls {
			license := s.Scrape(url)
			select {
			case out <- license:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func MergeErrors(cs ...<-chan error) <-chan error {
	var wg sync.WaitGroup
	out := make(chan error, len(cs))
	output := func(c <-chan error) {
		for n := range c {
			out <- n
		}
		wg.Done()
	}
	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}
	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func WaitForPipeline(errs ...<-chan error) error {
	errc := MergeErrors(errs...)
	for err := range errc {
		if err != nil {
			return err
		}
	}
	return nil
}
