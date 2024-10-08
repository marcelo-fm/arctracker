package gui

import (
	"log"
	"strings"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/lang"
	"fyne.io/fyne/v2/theme"
	"fyne.io/fyne/v2/widget"
)

func NewOpenFolderDialog(folder binding.String, w fyne.Window) fyne.CanvasObject {
	openFolderDialog := dialog.NewFolderOpen(func(l fyne.ListableURI, err error) {
		if err != nil {
			log.Println(err)
			return
		}
		if l == nil {
			log.Println("cancelled")
			return
		}
		folder.Set(strings.TrimPrefix(l.String(), "file://"))
	}, w)
	openFolderDialog.Resize(fyne.NewSize(1024, 720))
	openFolderButton := widget.NewButtonWithIcon(lang.L("Select Folder"), theme.FolderOpenIcon(), func() {
		openFolderDialog.Show()
	})
	centeredButton := JustifyCenter(openFolderButton)
	return centeredButton
}
