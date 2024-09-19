package scraper

import (
	"github.com/gocolly/colly"
	"github.com/gocolly/colly/extensions"
	"github.com/spf13/viper"
	"github.com/velebak/colly-sqlite3-storage/colly/sqlite3"
)

func NewCollector(s *sqlite3.Storage) (*colly.Collector, error) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(viper.GetString("cacheDir")),
		colly.AllowURLRevisit(),
	)
	extensions.RandomUserAgent(c)
	err := c.SetStorage(s)
	if err != nil {
		return nil, err
	}
	return c, nil
}
