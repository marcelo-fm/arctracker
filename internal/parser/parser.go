package parser

import (
	"fmt"
	"strings"

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
	return sequentialParse(searcher, s)
}

func parseCommand(match model.Match) string {
	fullCmd := strings.Trim(match.Text, " ")
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

func createURL(cmd string) string {
	pattern := viper.GetString("pattern")
	if !strings.HasPrefix(cmd, pattern+".") {
		log.Debug().Msgf("%s does not start with arcpy.", cmd)
		return ""
	}
	cmdArr := strings.Split(cmd, ".")
	lastIndex := len(cmdArr) - 1
	tool := parseTool(cmdArr[lastIndex])
	if tool == "" {
		return ""
	}
	var url string
	switch len(cmdArr) {
	case 3:
		module := parseModule(cmdArr[1])
		url = fmt.Sprintf("%s/%s", module, strings.ToLower(tool))
		return url + ".htm"
	case 2:
		if strings.Contains(cmdArr[1], "_") {
			cmd := strings.Split(cmdArr[1], "_")
			tool := parseTool(cmd[0])
			if tool == "" {
				return ""
			}
			module := parseModule(cmd[1])
			url = fmt.Sprintf("%s/%s", module, strings.ToLower(tool))
			return url + ".htm"
		}
		fallthrough
	default:
		return ""
	}
}
