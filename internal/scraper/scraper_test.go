package scraper

import (
	"os"
	"testing"

	"github.com/gocolly/colly"
	"github.com/stretchr/testify/assert"
)

func TestMain(m *testing.M) {
	status := m.Run()
	err := os.RemoveAll("./cache")
	if err != nil {
		status = 1
	}
	os.Exit(status)
}

func TestNew(t *testing.T) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir("./cache"),
	)
	s := New(c)
	assert.NotNil(t, s.c)
	assert.NotNil(t, s.l)
}

func TestSetupLicenseScraper(t *testing.T) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir("./cache"),
	)
	s := New(c)
	s.SetupLicenseScraper()

	assert.NotNil(t, s.c)
	assert.NotNil(t, s.l)
}

func TestScrape(t *testing.T) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir("./cache"),
	)
	s := New(c)
	s.SetupLicenseScraper()

	// Replace with a valid URL from pro.arcgis.com
	url := "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm"
	license := s.Scrape(url)

	// Replace with expected values
	assert.Equal(t, "Buffer (Analysis)", license.Title)
	assert.Equal(t, "arcpy.analysis.Buffer", license.Name)
	assert.Equal(t, "Limited", license.Basic)
	assert.Equal(t, "Limited", license.Standard)
	assert.Equal(t, "Yes", license.Advanced)
	assert.Equal(t, url, license.URL)
}
