//go:build !anon
// +build !anon

package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/lang"
	"fyne.io/fyne/v2/widget"
)

func NewBottomInfo() *fyne.Container {
	author := widget.NewLabel(lang.L("Author") + ": Marcelo Mesquita")
	github := widget.NewHyperlink("Github", nil)
	github.SetURLFromString("https://github.com/marcelo-fm")
	linkedin := widget.NewHyperlink("Linkedin", nil)
	linkedin.SetURLFromString("www.linkedin.com/in/marcelo-mesquita-535795233")
	return container.NewHBox(author, github, linkedin)
}
