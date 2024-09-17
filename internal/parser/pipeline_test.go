package parser

import (
	"os"
	"testing"

	"github.com/gocolly/colly"
	"github.com/gocolly/colly/extensions"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func TestPipelineParse(t *testing.T) {
	viper.SetDefault("loglevel", 3)
	viper.AutomaticEnv()
	zerolog.SetGlobalLevel(zerolog.Level(viper.GetInt("loglevel")))
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	cacheDir := viper.GetString("cacheDir")
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(cacheDir),
	)
	extensions.RandomUserAgent(c)
	s := scraper.New(c)
	srch := setupSearcher(t, false)
	licencas, err := pipelineParse(srch, &s)
	if err != nil {
		t.Fatalf("Error in parsing licenses: %s", err)
	}
	if len(licencas) == 0 {
		t.Error("Expected licenses, got none.")
	}
}

func BenchmarkPipelineParse(b *testing.B) {
	viper.SetDefault("loglevel", 3)
	viper.AutomaticEnv()
	zerolog.SetGlobalLevel(zerolog.Level(viper.GetInt("loglevel")))
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	cacheDir := viper.GetString("cacheDir")
	b.ResetTimer()
	for i := 0; i <= b.N; i++ {
		b.StopTimer()
		c := colly.NewCollector(
			colly.AllowedDomains("pro.arcgis.com"),
			colly.CacheDir(cacheDir),
		)
		extensions.RandomUserAgent(c)
		s := scraper.New(c)
		srch := setupSearcher(b, true)
		b.StartTimer()
		licencas, err := pipelineParse(srch, &s)
		if err != nil {
			b.Fatalf("Error in parsing licenses: %s", err)
		}
		if len(licencas) == 0 {
			b.Error("Expected licenses, got none.")
		}
	}
}
