package gui

import (
	"image/color"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/canvas"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/lang"
	"fyne.io/fyne/v2/theme"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/assets"
)

type forcedVariant struct {
	fyne.Theme
	variant fyne.ThemeVariant
}

func (f *forcedVariant) Color(name fyne.ThemeColorName, _ fyne.ThemeVariant) color.Color {
	return f.Theme.Color(name, f.variant)
}

func CreateToggleTheme(a fyne.App, imgContainer *fyne.Container) fyne.CanvasObject {
	var logo fyne.Resource
	switch a.Settings().ThemeVariant() {
	case theme.VariantDark:
		logo = assets.LogoDark
	case theme.VariantLight:
		logo = assets.LogoLight
	}
	image := canvas.NewImageFromResource(logo)
	image.ScaleMode = canvas.ImageScaleFastest
	image.FillMode = canvas.ImageFillOriginal
	imgContainer.RemoveAll()
	imgContainer.Add(image)
	themes := container.NewGridWithColumns(2,
		widget.NewButton(lang.L("Dark"), func() {
			a.Settings().SetTheme(&forcedVariant{Theme: theme.DefaultTheme(), variant: theme.VariantDark})
			image := canvas.NewImageFromResource(assets.LogoDark)
			image.ScaleMode = canvas.ImageScaleFastest
			image.FillMode = canvas.ImageFillOriginal
			imgContainer.RemoveAll()
			imgContainer.Add(image)
		}),
		widget.NewButton(lang.L("Light"), func() {
			a.Settings().SetTheme(&forcedVariant{Theme: theme.DefaultTheme(), variant: theme.VariantLight})
			image := canvas.NewImageFromResource(assets.LogoLight)
			image.ScaleMode = canvas.ImageScaleFastest
			image.FillMode = canvas.ImageFillOriginal
			imgContainer.RemoveAll()
			imgContainer.Add(image)
		}),
	)
	return themes
}
