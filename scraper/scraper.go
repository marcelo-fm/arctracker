package scraper

import (
	"strings"

	"github.com/gocolly/colly"
	"github.com/marcelo-fm/arctracker/model"
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
}

func (s *Scraper) Scrape(url string) model.License {
	s.c.Visit(url)
	defer func() { s.l = &model.License{} }()
	return *s.l
}
