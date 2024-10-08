package gui

import (
	"encoding/csv"
	"encoding/json"
	"fmt"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/layout"
	"fyne.io/fyne/v2/theme"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/internal/model"
)

func NewDownloadButtons(licenses []model.License, w fyne.Window) fyne.CanvasObject {
	buttons := container.NewHBox()
	jsonBtn := widget.NewButtonWithIcon("JSON", theme.DownloadIcon(), func() {
		dialog.ShowFileSave(func(writer fyne.URIWriteCloser, err error) {
			if err != nil {
				dialog.ShowError(err, w)
				return
			}
			if writer == nil {
				return
			}
			defer writer.Close()
			content, err := json.Marshal(licenses)
			if err != nil {
				dialog.ShowError(err, w)
				return
			}
			_, err = writer.Write(content)
			if err != nil {
				dialog.ShowError(err, w)
				return
			}
		}, w)
	})
	csvBtn := widget.NewButtonWithIcon("CSV", theme.DownloadIcon(), func() {
		saveFileDialog := dialog.NewFileSave(func(file fyne.URIWriteCloser, err error) {
			if err != nil {
				dialog.ShowError(err, w)
				return
			}
			if file == nil {
				return
			}
			defer file.Close()
			records := make([][]string, len(licenses)+1)
			records[0] = model.CSVHeaders()
			for i, l := range licenses {
				records[i+1] = l.ToRow()
			}
			csvWriter := csv.NewWriter(file)
			err = csvWriter.WriteAll(records)
			if err != nil {
				dialog.ShowError(err, w)
				return
			}
		}, w)
		saveFileDialog.Resize(fyne.NewSize(1024, 720))
		saveFileDialog.Show()
	})
	buttons.Add(jsonBtn)
	buttons.Add(csvBtn)
	return buttons
}

func NewLicenseContent(obj *fyne.Container, licenses []model.License, w fyne.Window) *fyne.Container {
	overview := widget.NewLabel(fmt.Sprintf("%d ferramentas encontradas", len(licenses)))
	downloads := NewDownloadButtons(licenses, w)
	header := container.NewGridWithColumns(3, container.NewHBox(downloads, layout.NewSpacer()), JustifyCenter(overview), layout.NewSpacer())
	tb := NewTable(licenses)
	border := container.NewBorder(header, nil, nil, nil, tb)
	obj.RemoveAll()
	obj.Add(border)
	return border
}
