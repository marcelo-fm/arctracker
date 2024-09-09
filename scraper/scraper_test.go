package scraper_test

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/gocolly/colly"
	"github.com/marcelo-fm/arctracker/scraper"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func TestMain(m *testing.M) {
	tmpDir, err := os.MkdirTemp("", "")
	if err != nil {
		log.Error().Err(err).Msg("Error in creating tempdir")
		os.Exit(1)
	}
	viper.SetDefault("cacheDir", tmpDir)
	status := m.Run()
	err = os.RemoveAll(tmpDir)
	if err != nil {
		log.Error().Err(err).Msg("Error in deleting tempdir")
		status = 1
	}
	os.Exit(status)
}

func TestScrape(t *testing.T) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir("./cache"),
	)
	s := scraper.New(c)
	s.SetupLicenseScraper()

	// Replace with a valid URL from pro.arcgis.com
	url := "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm"
	license := s.Scrape(url)

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
	tmpDir, err := os.MkdirTemp("", "")
	if err != nil {
		log.Error().Err(err).Msg("Error in creating tempdir")
		os.Exit(1)
	}
	cacheDir := filepath.Join(tmpDir, "cache")
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(cacheDir),
	)
	s := scraper.New(c)
	s.SetupLicenseScraper()

	// Replace with a valid URL from pro.arcgis.com
	url := "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm"
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		b.StopTimer()
		err = os.MkdirAll(cacheDir, os.ModePerm)
		if err != nil {
			log.Error().Err(err).Msg("Error in creating cacheDir")
			continue
		}
		b.StartTimer()
		s.Scrape(url)
		b.StopTimer()
		err = os.RemoveAll(tmpDir)
		if err != nil {
			log.Error().Err(err).Msg("Error in deleting tempdir")
			break
		}
		b.StartTimer()
	}
}
