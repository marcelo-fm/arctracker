package searcher

import (
	"os"
	"testing"

	"github.com/rs/zerolog"
	"github.com/spf13/viper"
)

func TestMain(m *testing.M) {
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("testdata", "../testdata/standard/")
	viper.SetDefault("loglevel", zerolog.WarnLevel)
	viper.AutomaticEnv()
	os.Exit(m.Run())
}
