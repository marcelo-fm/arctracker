package parser

import (
	"context"
	"fmt"
	"strings"
	"sync"
	"unicode"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

// Searcher é uma interface que define a busca de comandos arcpy.
// Search retorna um array de Match, que contém a palavra chave e o texto encontrado.
// O texto encontrado é a linha do arquivo de texto que contém a palavra chave.
// Comunmente, a busca é realizada em diretórios de arquivos python, ou por uma
// pipeline de busca de texto. A interface permite que a busca seja realizada a
// partir de diversas fontes de dados.
type Searcher interface {
	Search() ([]model.Match, error)
}

// Parser recebe um Searcher e um Scraper, e retorna uma lista com as licenças, ou nil
// se não houver nenhuma
func Parse(searcher Searcher, s *scraper.Scraper) ([]model.License, error) {
	contentArr, err := searcher.Search()
	if err != nil {
		return nil, err
	}
	baseURL := viper.GetString("baseURL")
	licenses := make([]model.License, 0, len(contentArr))
	for _, content := range contentArr {
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
	if licenses == nil {
		return nil, nil
	}
	return licenses, nil
}

// genContent gera o chanel de bytes, que representa cada achado da palavra chave com
// regex.
func genContent(ctx context.Context, in []model.Match) <-chan model.Match {
	out := make(chan model.Match)
	go func() {
		defer close(out)
		for _, content := range in {
			select {
			case out <- content:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func parseCommand(match model.Match) string {
	fullCmd := strings.Trim(match.Text, " ")
	log.Debug().Msgf("Cmd of %s: %s", match.Text, fullCmd)
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

func parseCommandChannel(ctx context.Context, in <-chan model.Match) <-chan string {
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
	case "gapro":
		return "geoanalytics-desktop"
	case "md":
		return "multidimension"
	case "nd":
		return "network-diagram"
	case "oi":
		return "oriented-imagery"
	case "transit":
		return "public-transit"
	case "rm":
		return "reality-mapping"
	case "stats":
		return "spatial-statistics"
	case "tn":
		return "trace-network"
	case "un":
		return "utility-networks"
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
		if strings.Contains(cmdArr[1], "_") {
			cmd := strings.Split(cmdArr[1], "_")
			tool := parseTool(cmd[0])
			module := parseModule(cmd[1])
			url = fmt.Sprintf("%s/%s", module, strings.ToLower(tool))
		} else {
			url = strings.ToLower(tool)
		}
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
