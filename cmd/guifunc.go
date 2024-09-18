package cmd

import (
	"os"
	"path/filepath"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"github.com/gocolly/colly"
	"github.com/gocolly/colly/extensions"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/ui/gui"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/viper"
)

func GUI() {
	viper.SetDefault("gui", true)
	var err error
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	if logLevel == -1 {
		zerolog.SetGlobalLevel(zerolog.Disabled)
	} else {
		zerolog.SetGlobalLevel(zerolog.Level(logLevel))
	}
	appConfigDir := viper.GetString("AppConfigDir")
	cacheDir := filepath.Join(appConfigDir, "cache")
	err = os.MkdirAll(cacheDir, 0755)
	if err != nil {
		log.Error().Err(err).Msg("Error creating cache directory.")
	}
	c := colly.NewCollector(
		colly.AllowedDomains("pro.arcgis.com"),
		colly.CacheDir(viper.GetString("cacheDir")),
		colly.AllowURLRevisit(),
	)
	extensions.RandomUserAgent(c)
	s := scraper.New(c)
	a := app.NewWithID("MarceloFM.ArcTracker")
	w := a.NewWindow("ArcTracker")
	greeter := gui.NewGreeterWindow(&s, a, w)
	w.SetContent(greeter)
	w.Resize(fyne.NewSize(1024, 720))
	w.ShowAndRun()
}
