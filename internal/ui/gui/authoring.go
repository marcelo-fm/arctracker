//go:build author
// +build author

package gui

import (
	"net/url"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func BottomInfo() *fyne.Container {
	author := widget.NewLabel("Autor: Marcelo Foschiera de Mesquita")
	ghLink, _ := url.ParseRequestURI("https://github.com/marcelo-fm")
	github := widget.NewHyperlink("Github", ghLink)
	return container.NewHBox(author, github)
}
