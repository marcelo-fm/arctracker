package parser

import (
	"os"
	"path/filepath"
	"runtime"
	"testing"

	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
	"github.com/velebak/colly-sqlite3-storage/colly/sqlite3"
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
	viper.SetDefault("storage", filepath.Join(appConfigDir, "results.db"))
	os.Exit(m.Run())
}

func setupSearcher(tb testing.TB, load bool) Searcher {
	tb.Helper()
	folder := "standard"
	if load {
		folder = "load"
	}
	testdataFolder := filepath.Join("../../testdata/", folder)
	switch runtime.GOOS {
	case "linux":
		return searcher.NewDefaultLinuxSearcher(false, testdataFolder)
	case "windows":
		return searcher.NewDefaultWindowsSearcher(false, testdataFolder)
	default:
		return searcher.NewRipgrep(false, testdataFolder)
	}
}

func TestSequentialParse(t *testing.T) {
	viper.SetDefault("loglevel", 3)
	viper.AutomaticEnv()
	zerolog.SetGlobalLevel(zerolog.Level(viper.GetInt("loglevel")))
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	storage := &sqlite3.Storage{Filename: viper.GetString("storage")}
	c, _ := scraper.NewCollector(storage)
	s := scraper.New(c, storage)
	srch := setupSearcher(t, false)
	licencas, err := sequentialParse(srch, &s)
	if err != nil {
		t.Fatalf("Error in parsing licenses: %s", err)
	}
	if len(licencas) == 0 {
		t.Error("Expected licenses, got none.")
	}
}

func BenchmarkSequentialParse(b *testing.B) {
	viper.SetDefault("loglevel", 3)
	viper.AutomaticEnv()
	zerolog.SetGlobalLevel(zerolog.Level(viper.GetInt("loglevel")))
	log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	b.ResetTimer()
	for i := 0; i <= b.N; i++ {
		b.StopTimer()
		storage := &sqlite3.Storage{Filename: viper.GetString("storage")}
		c, _ := scraper.NewCollector(storage)
		s := scraper.New(c, storage)
		srch := setupSearcher(b, true)
		b.StartTimer()
		licencas, err := sequentialParse(srch, &s)
		if err != nil {
			b.Fatalf("Error in parsing licenses: %s", err)
		}
		if len(licencas) == 0 {
			b.Error("Expected licenses, got none.")
		}
	}
}
