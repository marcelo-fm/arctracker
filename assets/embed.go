package assets

import (
	"embed"
	"io/fs"
)

//go:embed *
var Assets embed.FS

func LoadResource(name string) ([]byte, error) {
	return fs.ReadFile(Assets, name)
}
