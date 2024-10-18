package gui_test

import (
	"os"
	"path/filepath"
	"testing"

	"github.com/spf13/viper"
)

func TestMain(m *testing.M) {
	var err error
	viper.SetDefault("gui", true)
	viper.SetDefault("pattern", "arcpy")
	viper.SetDefault("baseURL", "https://pro.arcgis.com/en/pro-app/latest/tool-reference/")
	if err != nil {
		os.Exit(1)
	}
	configDir, err := os.UserConfigDir()
	if err != nil {
		os.Exit(1)
	}
	appConfigDir := filepath.Join(configDir, "arctracker")
	viper.SetDefault("appConfigDir", appConfigDir)
	err = os.MkdirAll(appConfigDir, 0755)
	if err != nil {
		os.Exit(1)
	}
	cacheDir := filepath.Join(appConfigDir, "cache")
	err = os.MkdirAll(cacheDir, 0755)
	if err != nil {
		os.Exit(1)
	}
	viper.SetDefault("cacheDir", cacheDir)
	viper.SetDefault("storage", filepath.Join(appConfigDir, "results.db"))
	viper.AddConfigPath(appConfigDir)
	os.Exit(m.Run())
}
