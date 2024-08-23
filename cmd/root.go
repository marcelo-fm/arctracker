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
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/charmbracelet/bubbles/table"
	"github.com/gocolly/colly"
	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/marcelo-fm/arctracker/internal/ui"
	"github.com/rs/zerolog"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var (
	cfgFile  string
	isJSON   bool
	isCSV    bool
	logLevel int
)

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "arctracker",
	Short: "Track your ArcGIS License requirements.",
	Long: `Track your ArcGIS License and extension requirements in your project.

ArcTracker analyses your licensing requirements by categorizing yout arcpy
tools used.`,
	Run: func(cmd *cobra.Command, args []string) {
		zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
		zerolog.SetGlobalLevel(zerolog.Level(logLevel))
		if len(args) == 0 {
			reader := bufio.NewReader(os.Stdin)
			content, err := io.ReadAll(reader)
			cobra.CheckErr(err)
			c := colly.NewCollector(
				colly.AllowedDomains("pro.arcgis.com"),
				colly.CacheDir("./cache"),
			)
			namespace := bytes.Split(content[0:len(content)-1], []byte("."))
			url := fmt.Sprintf("https://pro.arcgis.com/en/pro-app/latest/tool-reference/%s/%s.htm", string(namespace[1]), strings.ToLower(string(namespace[2])))
			s := scraper.New(c)
			s.SetupLicenseScraper()
			l := s.Scrape(url)
			jsonData, err := json.Marshal(&l)
			cobra.CheckErr(err)
			fmt.Println(string(jsonData))
			return
		}
		path := args[0]
		c := colly.NewCollector(
			colly.AllowedDomains("pro.arcgis.com"),
			colly.CacheDir("./cache"),
		)
		s := scraper.New(c)
		licenses, err := searcher.Search(path, &s)
		cobra.CheckErr(err)
		if isJSON {
			jsonData, err := json.Marshal(&licenses)
			cobra.CheckErr(err)
			fmt.Println(string(jsonData))
			return
		}
		tbRows := make([]table.Row, len(licenses))
		for i, l := range licenses {
			tbRows[i] = l.ToRow()
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
	rootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.arctracker.yaml)")
	rootCmd.PersistentFlags().IntVar(&logLevel, "loglevel", 4, "log level")
	rootCmd.Flags().BoolVar(&isJSON, "json", false, "output the result as a json")
	rootCmd.Flags().BoolVar(&isCSV, "csv", false, "output the result as a csv")
}

func initConfig() {
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	if cfgFile != "" {
		viper.SetConfigFile(cfgFile)
	} else {
		// Find configDir directory.
		configDir, err := os.UserConfigDir()
		cobra.CheckErr(err)

		// Search config in home directory with name ".arctracker" (without extension).
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
