package searcher_test

import (
	"runtime"
	"testing"

	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/rs/zerolog"
	"github.com/spf13/viper"
)

func TestNewGrep(t *testing.T) {
	if runtime.GOOS != "linux" {
		t.Skip("Invalid OS for testing this function. Skipping...")
	}
	zerolog.SetGlobalLevel(zerolog.InfoLevel)
	searcher := searcher.NewGrep(true, "")
	if searcher == nil {
		t.Fatal("Expected Ripgrep struct, got nil.")
	}
}

func TestGrepSearchWithPath(t *testing.T) {
	if runtime.GOOS != "linux" {
		t.Skip("Invalid OS for testing this function. Skipping...")
	}
	zerolog.SetGlobalLevel(zerolog.InfoLevel)
	path := viper.GetString("testdata")
	searcher := searcher.NewGrep(false, path)
	matches, err := searcher.Search()
	if err != nil {
		t.Fatalf("Error in searching in path %s", path)
	}
	if len(matches) == 0 {
		t.Error("Expected matches, but got zero")
	}
}

func BenchmarkGrepSearch(b *testing.B) {
	if runtime.GOOS != "linux" {
		b.Skip("Invalid OS for testing this function. Skipping...")
	}
	path := viper.GetString("testdata")
	searcher := searcher.NewGrep(false, path)
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
