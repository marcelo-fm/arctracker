package gui

import (
	"errors"
	"fmt"
	"os"
	"runtime"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/internal/parser"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/searcher"
)

func NewGreeterWindow(s *scraper.Scraper, a fyne.App, w fyne.Window) fyne.CanvasObject {
	display := container.NewStack()
	isStdin := false
	var srch parser.Searcher
	folder := binding.NewString()
	folderEntry := widget.NewEntryWithData(folder)
	openFolderButton := NewOpenFolderDialog(folder, w)
	startProcess := JustifyCenter(widget.NewButton("Buscar Licenças", func() {
		path, err := folder.Get()
		if err != nil {
			errd := dialog.NewError(err, w)
			errd.Show()
			return
		}
		if path == "" {
			errd := dialog.NewError(errors.New("Escolha um diretório válido!"), w)
			errd.Show()
			return
		}
		if searcher.HasRipgrepDeps() {
			srch = searcher.NewRipgrep(isStdin, path)
		} else {
			switch runtime.GOOS {
			case "linux":
				srch = searcher.NewGrep(isStdin, path)
			case "windows":
				srch = searcher.NewSelectString(isStdin, path)
			default:
				fmt.Println("No searcher found, please install ripgrep to run the program.")
				os.Exit(1)
			}
		}
		licenses, err := parser.Parse(srch, s)
		if err != nil {
			dialog.NewError(err, w)
			return
		}
		_ = NewLicenseContent(display, licenses, w)
	}))
	greeter := container.NewBorder(container.NewGridWithColumns(
		3,
		layout.NewSpacer(),
		container.NewVBox(
			JustifyCenter(
				container.NewHBox(
					openFolderButton,
					startProcess,
				)),
			folderEntry,
		),
	),
		nil, nil, nil, display)
	return AddHeader(a, greeter)
}
