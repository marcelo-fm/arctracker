//go:build gui
// +build gui

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
	"github.com/spf13/cobra"
)

// cliCmd represents the cli command
var cliCmd = &cobra.Command{
	Use:   "cli",
	Short: "Track your ArcGIS License requirements.",
	Long: `Track your ArcGIS License and extension requirements in your project.
ArcTracker analyses your licensing requirements by categorizing your arcpy
tools used.

To use it, just pass the path of the folder with arcpy python code, or use the
tool within a pipeline by calling it without arguments. Doing so will parse the
result of the previous command in the pipeline and return the arcpy tools present
in it.`,
	Run: func(cmd *cobra.Command, args []string) {
		CLI(args)
	},
}

func init() {
	rootCmd.AddCommand(cliCmd)
	cliCmd.PersistentFlags().IntVar(&logLevel, "loglevel", 4, "log level")
	cliCmd.Flags().BoolVar(&isJSON, "json", false, "output the result as a JSON")
	cliCmd.Flags().BoolVar(&isCSV, "csv", false, "output the result as a CSV")
	cliCmd.MarkFlagsMutuallyExclusive("json", "csv")
	cliCmd.Flags().StringVar(&csvDelim, "delimiter", ",", "CSV field delimiter")
	cliCmd.Flags().StringVar(&output, "output", "", "write the JSON or CSV output in a file")
}
