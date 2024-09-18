package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/layout"
	"github.com/marcelo-fm/arctracker/assets"
	"github.com/rs/zerolog/log"
)

func AddHeader(a fyne.App, content fyne.CanvasObject) fyne.CanvasObject {
	var logo fyne.CanvasObject
	logo = layout.NewSpacer()
	f, err := assets.Assets.Open("arctracker-logo.png")
	if err != nil {
		log.Debug().Err(err).Msg("Error in reading logo file")
		logo = canvas.NewImageFromReader(f, "arctracker-logo")
	}
	themes := CreateToggleTheme(a)
	header := container.NewHBox(
		logo,
		layout.NewSpacer(),
		JustifyCenter(themes),
	)
	return container.NewPadded(container.NewBorder(header, BottomInfo(), nil, nil, content))
}
