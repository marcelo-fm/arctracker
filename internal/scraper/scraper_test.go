package scraper_test

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/gocolly/colly"
	"github.com/gocolly/colly/extensions"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func TestMain(m *testing.M) {
	configDir, err := os.UserConfigDir()
	appConfigDir := filepath.Join(configDir, "arctracker")
	viper.SetDefault("appConfigDir", appConfigDir)
	err = os.MkdirAll(appConfigDir, 0755)
	cacheDir := filepath.Join(appConfigDir, "cache")
	err = os.MkdirAll(cacheDir, 0755)
	if err != nil {
		log.Error().Err(err).Msg("Error creating cache directory.")
	}
	viper.SetDefault("cacheDir", cacheDir)
	os.Exit(m.Run())
}

func TestScrape(t *testing.T) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(viper.GetString("cacheDir")),
	)
	extensions.RandomUserAgent(c)
	s := scraper.New(c)
	s.SetupLicenseScraper()

	// Replace with a valid URL from pro.arcgis.com
	url := "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm"
	license, err := s.Scrape(url)
	if err != nil {
		t.Fatalf("Error in scraping data: %v", err)
	}

	// Replace with expected values
	if license.Title != "Buffer (Analysis)" {
		t.Errorf("Expected license.Title to be 'Buffer (Analysis)', got %v", license.Title)
	}

	if license.Name != "arcpy.analysis.Buffer" {
		t.Errorf("Expected license.Name to be 'arcpy.analysis.Buffer', got %v", license.Name)
	}

	if license.Basic != "Limited" {
		t.Errorf("Expected license.Basic to be 'Limited', got %v", license.Basic)
	}

	if license.Standard != "Limited" {
		t.Errorf("Expected license.Standard to be 'Limited', got %v", license.Standard)
	}

	if license.Advanced != "Yes" {
		t.Errorf("Expected license.Advanced to be 'Yes', got %v", license.Advanced)
	}

	if license.URL != url {
		t.Errorf("Expected license.URL to be %v, got %v", url, license.URL)
	}
}

func BenchmarkScrape(b *testing.B) {
	cacheDir := viper.GetString("cacheDir")
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(cacheDir),
	)
	extensions.RandomUserAgent(c)
	s := scraper.New(c)
	s.SetupLicenseScraper()

	// Replace with a valid URL from pro.arcgis.com
	url := "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm"
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		s.Scrape(url)
	}
}
