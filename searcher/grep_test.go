package searcher

import (
	"runtime"
	"testing"
)

func TestNewGrep(t *testing.T) {
	if runtime.GOOS != "linux" {
		t.Skip("Invalid OS for testing this function. Skipping...")
	}
	searcher := NewGrep(true, "")
	if searcher == nil {
		t.Fatal("Expected Ripgrep struct, got nil.")
	}
}

func TestGrepSearchWithPath(t *testing.T) {
	if runtime.GOOS != "linux" {
		t.Skip("Invalid OS for testing this function. Skipping...")
	}
	path := "../../testdata"
	searcher := NewGrep(false, path)
	matches, err := searcher.Search()
	if err != nil {
		t.Fatalf("Error in searching in path %s", path)
	}
	if len(matches) == 0 {
		t.Error("Expected matches, but got zero")
	}
}
