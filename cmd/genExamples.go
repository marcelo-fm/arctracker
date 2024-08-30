//go:build !prod

package cmd

import (
	"os"
	"strings"

	"github.com/gocolly/colly"
	"github.com/gocolly/colly/extensions"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
	"github.com/spf13/cobra"
)

// genExamplesCmd represents the genExamples command
var genExamplesCmd = &cobra.Command{
	Use:   "genExamples",
	Short: "Generate code examples from arcgis documentation.",
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
		zerolog.SetGlobalLevel(zerolog.Level(logLevel))
		path := args[0]
		err := os.MkdirAll(path, 0766)
		cobra.CheckErr(err)
		c := colly.NewCollector(
			colly.AllowedDomains("pro.arcgis.com"),
			colly.CacheDir("./_examples_cache"),
		)
		extensions.RandomUserAgent(c)
		c.OnHTML("div[class=codeblockbody]", func(e *colly.HTMLElement) {
			log.Info().Str("url", e.Request.URL.String()).Msg("Code block found.")
			exampleCode := e.ChildText("pre")
			log.Debug().Str("exampleCode", exampleCode).Msg("Example code found.")
			pathArr := strings.Split(e.Request.URL.Path, "/")
			filename := strings.Split(pathArr[len(pathArr)-1], ".")[0] + ".py"
			err := os.WriteFile(path+"/"+filename, []byte(exampleCode), 0644)
			if err != nil {
				log.Error().Err(err).Msg("Error writing file.")
			} else {
				log.Info().Str("filename", filename).Msg("File written.")
			}
		})
		c.OnHTML("a[href]", func(e *colly.HTMLElement) {
			link := e.Attr("href")
			if !strings.Contains(link, "tool-reference") {
				return
			}
			log.Debug().Str("link", link).Msg("Visiting link")
			c.Visit(e.Request.AbsoluteURL(link))
		})
		c.OnError(func(r *colly.Response, err error) {
			log.Error().Err(err).Str("url", r.Request.URL.String()).Msg("Error visiting URL")
		})
		c.OnResponse(func(r *colly.Response) {
			log.Debug().Str("url", r.Request.URL.String()).Msg("Visited URL")
		})
		err = c.Visit("https://pro.arcgis.com/en/pro-app/latest/get-started/license-levels.htm")
		if err != nil {
			log.Error().Err(err).Msg("Error visiting root URL")
		}
	},
}

func init() {
	rootCmd.AddCommand(genExamplesCmd)
}
