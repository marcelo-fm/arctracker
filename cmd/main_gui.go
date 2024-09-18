//go:build gui
// +build gui

package cmd

import (
	"os"
	"path/filepath"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/lang"
	"github.com/gocolly/colly"
	"github.com/gocolly/colly/extensions"
	"github.com/marcelo-fm/arctracker/assets"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/ui/gui"
	"github.com/rs/zerolog"
	"github.com/spf13/viper"
)

func MainProcess() {
	viper.SetDefault("gui", true)
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	configDir, err := os.UserConfigDir()
	if err != nil {
		os.Exit(1)
	}
	appConfigDir := filepath.Join(configDir, "arctracker")
	viper.SetDefault("appConfigDir", appConfigDir)
	err = os.MkdirAll(appConfigDir, 0755)
	if err != nil {
		os.Exit(1)
	}
	cacheDir := filepath.Join(appConfigDir, "cache")
	err = os.MkdirAll(cacheDir, 0755)
	if err != nil {
		os.Exit(1)
	}
	viper.SetDefault("cacheDir", cacheDir)
	viper.AddConfigPath(appConfigDir)
	viper.SetConfigType("toml")
	viper.SetConfigName("config")
	viper.ReadInConfig()
	viper.AutomaticEnv()
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	zerolog.SetGlobalLevel(zerolog.Disabled)
	err = os.MkdirAll(cacheDir, 0755)
	if err != nil {
		os.Exit(1)
	}
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(viper.GetString("cacheDir")),
		colly.AllowURLRevisit(),
	)
	extensions.RandomUserAgent(c)
	s := scraper.New(c)
	a := app.NewWithID("MarceloFM.ArcTracker")
	lang.AddTranslationsFS(assets.Translations, "translation")
	w := a.NewWindow("ArcTracker")
	greeter := gui.NewGreeterWindow(&s, a, w)
	w.SetContent(greeter)
	w.Resize(fyne.NewSize(1024, 720))
	w.ShowAndRun()
}
