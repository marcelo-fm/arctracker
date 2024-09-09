package searcher

import (
	"os"
	"testing"

	"github.com/spf13/viper"
)

func TestMain(m *testing.M) {
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("testdata", "../testdata/")
	os.Exit(m.Run())
}
