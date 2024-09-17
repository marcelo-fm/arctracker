package searcher_test

import (
	"runtime"
	"testing"

	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/spf13/viper"
)

func TestNewFindstr(t *testing.T) {
	if runtime.GOOS != "windows" {
		t.Skip("Invalid OS for testing this function. Skipping...")
	}
	searcher := searcher.NewFindstr(true, "")
	if searcher == nil {
		t.Fatal("Expected Ripgrep struct, got nil.")
	}
}

func TestFindstrSearchWithPath(t *testing.T) {
	if runtime.GOOS != "windows" {
		t.Skip("Invalid OS for testing this function. Skipping...")
	}
	path := viper.GetString("testdata")
	searcher := searcher.NewFindstr(false, path)
	matches, err := searcher.Search()
	if err != nil {
		t.Fatalf("Error in searching in path %s", path)
	}
	if len(matches) == 0 {
		t.Error("Expected matches, but got zero")
	}
}
