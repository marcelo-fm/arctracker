package searcher_test

import (
	"testing"

	"github.com/marcelo-fm/arctracker/internal/searcher"
	"github.com/rs/zerolog"
	"github.com/spf13/viper"
)

func TestNewStandard(t *testing.T) {
	zerolog.SetGlobalLevel(zerolog.InfoLevel)
	searcher := searcher.NewStandard(false, "")
	if searcher == nil {
		t.Fatal("Expected GUI struct, got nil.")
	}
}

func TestGUISearchWithPath(t *testing.T) {
	zerolog.SetGlobalLevel(zerolog.InfoLevel)
	path := viper.GetString("testdata")
	searcher := searcher.NewStandard(false, path)
	matches, err := searcher.Search()
	if err != nil {
		t.Fatalf("Error in searching in path %s", path)
	}
	if len(matches) == 0 {
		t.Error("Expected matches, but got zero")
	}
}

func BenchmarkGUISearch(b *testing.B) {
	path := viper.GetString("testdata")
	searcher := searcher.NewStandard(false, path)
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
