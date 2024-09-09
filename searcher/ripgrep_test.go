package searcher_test

import (
	"runtime"
	"testing"

	"github.com/marcelo-fm/arctracker/searcher"
	"github.com/rs/zerolog"
	"github.com/spf13/viper"
)

func TestNewRipgrep(t *testing.T) {
	if !searcher.HasRipgrepDeps() {
		t.Skip("The OS does not have ripgrep or jq. Skipping...")
	}
	searcher := searcher.NewRipgrep(true, "")
	if searcher == nil {
		t.Fatal("Expected Ripgrep struct, got nil.")
	}
}

func TestRipgrepSearchWithPath(t *testing.T) {
	if !searcher.HasRipgrepDeps() {
		t.Skip("The OS does not have ripgrep or jq. Skipping...")
	}
	path := viper.GetString("testdata")
	searcher := searcher.NewRipgrep(false, path)
	matches, err := searcher.Search()
	if err != nil {
		t.Fatalf("Error in searching in path %s", path)
	}
	if len(matches) == 0 {
		t.Error("Expected matches, but got zero")
	}
}

func BenchmarkRipGrepSearch(b *testing.B) {
	if runtime.GOOS != "linux" {
		b.Skip("Invalid OS for testing this function. Skipping...")
	}
	path := viper.GetString("testdata")
	searcher := searcher.NewRipgrep(false, path)
	zerolog.SetGlobalLevel(zerolog.InfoLevel)
	b.ResetTimer()
	for i := 0; i <= b.N; i++ {
		matches, err := searcher.Search()
		b.StopTimer()
		if err != nil {
			b.Fatalf("Error in searching in path %s", path)
		}
		if len(matches) == 0 {
			b.Error("Expected matches, but got zero")
		}
		b.StartTimer()
	}
}
