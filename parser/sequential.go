package parser

import (
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
		log.Info().Msg("Done")
		log.Info().Msg("Scraping license information...")
		defer log.Info().Msg("Done")
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
