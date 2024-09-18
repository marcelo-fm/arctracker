package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
)

func JustifyCenter(obj fyne.CanvasObject) fyne.CanvasObject {
	return container.NewHBox(layout.NewSpacer(), obj, layout.NewSpacer())
}

func ItemsCenter(obj fyne.CanvasObject) fyne.CanvasObject {
	return container.NewVBox(layout.NewSpacer(), obj, layout.NewSpacer())
}
