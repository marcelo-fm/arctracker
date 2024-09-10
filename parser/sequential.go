package parser

import (
	"strings"

	"github.com/marcelo-fm/arctracker/model"
	"github.com/marcelo-fm/arctracker/scraper"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

// Parser recebe um Searcher e um Scraper, e retorna uma lista com as licenças, ou nil
// se não houver nenhuma
func sequentialParse(searcher Searcher, s *scraper.Scraper) ([]model.License, error) {
	log.Info().Msg("Searching for arcpy commands...")
	contentArr, err := searcher.Search()
	if err != nil {
		return nil, err
	}
	log.Info().Msg("Done")
	log.Info().Msg("Parsing arcpy commands...")
	baseURL := viper.GetString("baseURL")
	urls := make([]string, 0, len(contentArr))
	for _, content := range contentArr {
		cmd := parseCommand(content)
		if cmd == "" {
			log.Debug().Msgf("There is no command in match: %s", content.Text)
			continue
		}
		log.Debug().Str("Cmd", cmd).Send()
		url := createURL(cmd)
		if url == "" {
			continue
		}
		log.Debug().Str("URL", url).Send()
		urls = append(urls, url)
	}
	uniqueURLs := removeDuplicates(urls)
	log.Debug().Msgf("%v", strings.Join(uniqueURLs, "\n"))
	licenses := make([]model.License, 0, len(uniqueURLs))
	for _, url := range uniqueURLs {
		s.SetupLicenseScraper()
		log.Info().Msg("Scraping license information...")
		scrapeURL := baseURL + url
		license, err := s.Scrape(scrapeURL)
		if err != nil {
			log.Error().Err(err).Msgf("Error in scraping url %s", scrapeURL)
			return nil, err
		}
		log.Info().Msg("Done")
		if license.Title == "" && license.Name == "" {
			log.Debug().Msg("License does not have Title and Name")
			continue
		}
		log.Debug().Msgf("Appending %s to licenses", license.Name)
		licenses = append(licenses, license)
	}
	if licenses == nil {
		return nil, nil
	}
	return licenses, nil
}

func removeDuplicates(strings []string) []string {
	uniqueStrings := make(map[string]bool)
	result := []string{}

	for _, str := range strings {
		if !uniqueStrings[str] {
			uniqueStrings[str] = true
			result = append(result, str)
		}
	}

	return result
}
