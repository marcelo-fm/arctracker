/*
Copyright © 2024 MARCELO MESQUITA

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cmd

import (
	"bufio"
	"encoding/csv"
	"encoding/json"
	"os"
	"path/filepath"

	"github.com/charmbracelet/bubbles/table"
	"github.com/gocolly/colly"
	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/marcelo-fm/arctracker/internal/ui"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var (
	cfgFile  string
	isJSON   bool
	isCSV    bool
	csvDelim string
	output   string
	logLevel int
)

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "arctracker",
	Short: "Track your ArcGIS License requirements.",
	Long: `Track your ArcGIS License and extension requirements in your project.

ArcTracker analyses your licensing requirements by categorizing yout arcpy
tools used.`,
	Args: cobra.RangeArgs(0, 1),
	Run: func(cmd *cobra.Command, args []string) {
		var err error
		var licenses []model.License
		zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
		zerolog.SetGlobalLevel(zerolog.Level(logLevel))
		c := colly.NewCollector(
			colly.AllowedDomains("pro.arcgis.com"),
			colly.CacheDir("./cache"),
		)
		s := scraper.New(c)
		if len(args) == 0 {
			reader := bufio.NewReader(os.Stdin)
			licenses, err = searcher.SearchWithStdin(reader, &s)
		} else {
			path := args[0]
			licenses, err = searcher.SearchWithPath(path, &s)
		}
		cobra.CheckErr(err)
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
	},
}

type License struct {
	Title    string `json:"title"`
	Name     string `json:"name"`
	Basic    string `json:"basic"`
	Standard string `json:"standard"`
	Advanced string `json:"advanced"`
	Url      string `json:"url"`
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	cobra.OnInitialize(initConfig)
	rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is in config directory)")
	rootCmd.PersistentFlags().IntVar(&logLevel, "loglevel", 4, "log level")
	rootCmd.Flags().BoolVar(&isJSON, "json", false, "output the result as a JSON")
	rootCmd.Flags().BoolVar(&isCSV, "csv", false, "output the result as a CSV")
	rootCmd.MarkFlagsMutuallyExclusive("json", "csv")
	rootCmd.Flags().StringVar(&csvDelim, "delimiter", ",", "CSV field delimiter")
	rootCmd.Flags().StringVar(&output, "output", "", "write the JSON or CSV output in a file")
}

func initConfig() {
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	if cfgFile != "" {
		viper.SetConfigFile(cfgFile)
	} else {
		configDir, err := os.UserConfigDir()
		cobra.CheckErr(err)
		appConfigDir := filepath.Join(configDir, "arctracker")
		err = os.MkdirAll(appConfigDir, 0755)
		cobra.CheckErr(err)
		viper.AddConfigPath(appConfigDir)
		viper.SetConfigType("toml")
		viper.SetConfigName("config")
	}
	_ = viper.ReadInConfig()
	viper.AutomaticEnv()
}
