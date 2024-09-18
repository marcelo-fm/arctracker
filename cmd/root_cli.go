//go:build !gui
// +build !gui

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
	"os"
	"path/filepath"

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
ArcTracker analyses your licensing requirements by categorizing your arcpy
tools used.

To use it, just pass the path of the folder with arcpy python code, or use the
tool within a pipeline by calling it without arguments. Doing so will parse the
result of the previous command in the pipeline and return the arcpy tools present
in it.`,
	Args: cobra.RangeArgs(0, 1),
	Run: func(cmd *cobra.Command, args []string) {
		CLI(args)
	},
}

func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	cobra.OnInitialize(initConfig)
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
		viper.SetDefault("appConfigDir", appConfigDir)
		err = os.MkdirAll(appConfigDir, 0755)
		cobra.CheckErr(err)
		cacheDir := filepath.Join(appConfigDir, "cache")
		err = os.MkdirAll(cacheDir, 0755)
		if err != nil {
			log.Error().Err(err).Msg("Error creating cache directory.")
			cobra.CheckErr(err)
		}
		viper.SetDefault("cacheDir", cacheDir)
		viper.AddConfigPath(appConfigDir)
		viper.SetConfigType("toml")
		viper.SetConfigName("config")
	}
	_ = viper.ReadInConfig()
	viper.AutomaticEnv()
}
