package cmd

import (
	"os"
	"path/filepath"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/lang"
	"github.com/marcelo-fm/arctracker/assets"
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
	scraper.InitStorage()
	storage := scraper.NewStorage()
	c, err := scraper.NewCollector(storage)
	if err != nil {
		log.Error().Err(err).Msg("Error in setting storage")
		os.Exit(1)
	}
	s := scraper.New(c, storage)
	a := app.NewWithID("MarceloFM.ArcTracker")
	lang.AddTranslationsFS(assets.Translations, "translation")
	w := a.NewWindow("ArcTracker")
	greeter := gui.NewGreeterWindow(&s, a, w)
	w.SetContent(greeter)
	w.Resize(fyne.NewSize(1024, 720))
	w.ShowAndRun()
}
