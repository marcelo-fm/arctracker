package parser

import (
	"context"
	"sync"

	"github.com/marcelo-fm/arctracker/model"
)

// genContent gera o chanel de bytes, que representa cada achado da palavra chave com
// regex.
func genContent(ctx context.Context, in []model.Match) <-chan model.Match {
	out := make(chan model.Match)
	go func() {
		defer close(out)
		for _, content := range in {
			select {
			case out <- content:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func parseCommandChannel(ctx context.Context, in <-chan model.Match) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for match := range in {
			cmd := parseCommand(match)
			select {
			case out <- cmd:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func createURLChannel(ctx context.Context, in <-chan string) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)
		for cmd := range in {
			url := createURL(cmd)
			if url == "" {
				continue
			}
			select {
			case out <- url:
			case <-ctx.Done():
				return
			}
		}
	}()
	return out
}

func mergeErrors(cs ...<-chan error) <-chan error {
	var wg sync.WaitGroup
	out := make(chan error, len(cs))
	output := func(c <-chan error) {
		for n := range c {
			out <- n
		}
		wg.Done()
	}
	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}
	go func() {
		wg.Wait()
		close(out)
	}()
	return out
}

func waitForPipeline(errs ...<-chan error) error {
	errc := mergeErrors(errs...)
	for err := range errc {
		if err != nil {
			return err
		}
	}
	return nil
}
