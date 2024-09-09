package searcher

import (
	"testing"

	"github.com/spf13/viper"
)

func TestNewRipgrep(t *testing.T) {
	if !HasRipgrepDeps() {
		t.Skip("The OS does not have ripgrep or jq. Skipping...")
	}
	searcher := NewRipgrep(true, "")
	if searcher == nil {
		t.Fatal("Expected Ripgrep struct, got nil.")
	}
}

func TestRipgrepSearchWithPath(t *testing.T) {
	if !HasRipgrepDeps() {
		t.Skip("The OS does not have ripgrep or jq. Skipping...")
	}
	path := viper.GetString("testdata")
	searcher := NewRipgrep(false, path)
	matches, err := searcher.Search()
	if err != nil {
		t.Fatalf("Error in searching in path %s", path)
	}
	if len(matches) == 0 {
		t.Error("Expected matches, but got zero")
	}
}
