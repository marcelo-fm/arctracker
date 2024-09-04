package scraper

import (
	"os"
	"testing"

	"github.com/gocolly/colly"
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
	if s.c == nil {
		t.Error("collector is nil, expected a Collector")
	}
	if s.l == nil {
		t.Error("license is nil, expected a empty License model")
	}
	if s.l.Name != "" || s.l.Title != "" {
		t.Error("expected an empty License")
	}
}

func TestSetupLicenseScraper(t *testing.T) {
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir("./cache"),
	)
	s := New(c)
	s.SetupLicenseScraper()

	if s.c == nil {
		t.Error("Expected s.c not to be nil")
	}

	if s.l == nil {
		t.Error("Expected s.l not to be nil")
	}
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
