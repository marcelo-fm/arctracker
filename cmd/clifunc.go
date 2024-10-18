package cmd

import (
	"encoding/csv"
	"encoding/json"
	"os"
	"path/filepath"

	"github.com/charmbracelet/bubbles/table"
	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/parser"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/marcelo-fm/arctracker/internal/ui"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

func CLI(args []string) {
	var err error
	var licenses []model.License
	var isStdin bool
	var path string
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
	if len(args) == 0 {
		isStdin = true
	} else {
		path = args[0]
	}
	srch := searcher.NewGUI(path)
	licenses, err = parser.Parse(srch, &s)
	if err != nil {
		log.Error().Err(err).Msg("Error in parsing licenses.")
		cobra.CheckErr(err)
	}

	writer := os.Stdout
	if output != "" {
		file, err := os.Create(output)
		cobra.CheckErr(err)
		defer file.Close()
		writer = file
	}
	if isJSON {
		encoder := json.NewEncoder(writer)
		err := encoder.Encode(&licenses)
		cobra.CheckErr(err)
		return
	}
	if isCSV {
		records := make([][]string, len(licenses)+1)
		records[0] = model.CSVHeaders()
		for i, l := range licenses {
			records[i+1] = l.ToRow()
		}
		w := csv.NewWriter(writer)
		if len(csvDelim) == 1 {
			w.Comma = rune(csvDelim[0])
		}
		w.WriteAll(records)
		if err := w.Error(); err != nil {
			log.Fatal().Err(err).Msg("error writing csv")
		}
		return
	}
	tbRows := make([]table.Row, len(licenses))
	for i, l := range licenses {
		tbRows[i] = l.ToTableRow()
	}
	tb := ui.New(model.LicenseColumns(), tbRows)
	tb.Run()
}
