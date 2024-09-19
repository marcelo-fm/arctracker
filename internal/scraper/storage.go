package scraper

import (
	"os"

	"github.com/spf13/viper"
	"github.com/velebak/colly-sqlite3-storage/colly/sqlite3"
)

func NewStorage() *sqlite3.Storage {
	return &sqlite3.Storage{
		Filename: viper.GetString("storage"),
	}
}

func InitStorage() {
	path := viper.GetString("appConfigDir")
	if _, err := os.Stat(path); os.IsNotExist(err) {
		s := &sqlite3.Storage{
			Filename: viper.GetString("storage"),
		}
		s.Close()
	}
}
