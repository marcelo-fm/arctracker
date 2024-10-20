package gui

import (
	"errors"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/lang"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/internal/model"
	"github.com/marcelo-fm/arctracker/internal/parser"
	"github.com/marcelo-fm/arctracker/internal/scraper"
	"github.com/marcelo-fm/arctracker/internal/searcher"
)

func NewGreeterWindow(s *scraper.Scraper, a fyne.App, w fyne.Window) fyne.CanvasObject {
	loading := widget.NewProgressBarInfinite()
	loadingContainer := ItemsCenter(container.NewGridWithColumns(3, layout.NewSpacer(), loading, layout.NewSpacer()))
	display := container.NewStack(loadingContainer)
	tb := container.NewStack()
	display.Add(tb)
	loading.Hide()
	folder := binding.NewString()
	folderEntry := widget.NewEntryWithData(folder)
	openFolderButton := NewOpenFolderDialog(folder, w)
	startProcess := JustifyCenter(widget.NewButton(lang.L("Search Licenses"), func() {
		path, err := folder.Get()
		if err != nil {
			errd := dialog.NewError(err, w)
			errd.Show()
			return
		}
		if path == "" {
			errd := dialog.NewError(errors.New(lang.L("Pick a valid folder!")), w)
			errd.Show()
			return
		}
		srch := searcher.NewStandard(false, path)
		licensesc := make(chan []model.License)
		errc := make(chan error)
		tb.Hide()
		loading.Show()
		loading.Start()
		go func() {
			licenses, err := parser.Parse(srch, s)
			licensesc <- licenses
			errc <- err
		}()
		go func() {
			var licenses []model.License
			var err error
			select {
			case licenses = <-licensesc:
			case err = <-errc:
			}
			loading.Stop()
			loading.Hide()
			if err != nil {
				dialog.NewError(err, w)
				return
			}
			NewLicenseContent(tb, licenses, w)
			tb.Show()
		}()
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
