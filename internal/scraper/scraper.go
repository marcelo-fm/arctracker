package scraper

import (
	"strings"

	"github.com/gocolly/colly"
	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/rs/zerolog/log"
)

func New(c *colly.Collector) Scraper {
	return Scraper{
		c: c,
		l: &model.License{},
	}
}

type Scraper struct {
	c *colly.Collector
	l *model.License
}

func (s *Scraper) SetupLicenseScraper() {
	s.c.OnHTML("h1", func(e *colly.HTMLElement) {
		s.l.Title = e.Text
	})
	s.c.OnHTML("pre[purpose=gptoolexpression]", func(e *colly.HTMLElement) {
		funcArr := strings.Split(e.Text, "(")
		s.l.Name = funcArr[0]
	})
	s.c.OnHTML("div[id=L_]", func(e *colly.HTMLElement) {
		e.ForEach("li", func(i int, e *colly.HTMLElement) {
			licenseType := strings.Split(e.Text, ": ")
			switch licenseType[0] {
			case "Basic":
				s.l.Basic = licenseType[1]
			case "Standard":
				s.l.Standard = licenseType[1]
			case "Advanced":
				s.l.Advanced = licenseType[1]
			}
		})
		s.l.URL = e.Request.AbsoluteURL("")
	})
	s.c.OnError(func(r *colly.Response, err error) {
		if err.Error() != "Not Found" {
			log.Error().Err(err).Str("url", r.Request.URL.String()).Msg("Error visiting URL")
		}
	})
	s.c.OnResponse(func(r *colly.Response) {
		log.Debug().Str("url", r.Request.URL.String()).Msg("Visited URL")
	})
}

func (s *Scraper) Scrape(url string) (model.License, error) {
	log.Debug().Msgf("Visiting %s", url)
	err := s.c.Visit(url)
	if err != nil {
		if err.Error() == "Not Found" {
			err = nil
		}
	}
	defer func() { s.l = &model.License{} }()
	return *s.l, err
}
