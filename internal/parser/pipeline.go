package parser

import (
	"context"
	"strings"
	"sync"

	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func pipelineParse(searcher Searcher, s *scraper.Scraper) ([]model.License, error) {
	log.Info().Msg("Searching for arcpy commands...")
	contentArr, err := searcher.Search()
	if err != nil {
		return nil, err
	}
	log.Info().Msg("Done")
	log.Info().Msg("Parsing arcpy commands...")
	baseURL := viper.GetString("baseURL")
	urls := make([]string, 0, len(contentArr))
	ctx := context.TODO()
	matchc := genContent(ctx, contentArr)
	cmdc := parseCommandChannel(ctx, matchc)
	urlc := createURLChannel(ctx, cmdc)
	for u := range urlc {
		urls = append(urls, u)
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

func parseCommandChannel(ctx context.Context, in <-chan model.Match) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for match := range in {
			cmd := parseCommand(match)
			if cmd == "" {
				continue
			}
			select {
			case out <- cmd:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
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

func mergeErrors(cs ...<-chan error) <-chan error {
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

func waitForPipeline(errs ...<-chan error) error {
	errc := mergeErrors(errs...)
	for err := range errc {
		if err != nil {
			return err
		}
	}
	return nil
}
