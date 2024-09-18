package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
)

func AddHeader(a fyne.App, content fyne.CanvasObject) fyne.CanvasObject {
	imgContainer := container.NewStack()
	themes := CreateToggleTheme(a, imgContainer)
	header := container.NewHBox(
		imgContainer,
		layout.NewSpacer(),
		ItemsCenter(JustifyCenter(themes)),
	)
	return container.NewPadded(container.NewBorder(header, BottomInfo(), nil, nil, content))
}
