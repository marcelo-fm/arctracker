//go:build anon
// +build anon

package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
)

func NewBottomInfo() *fyne.Container {
	return container.NewHBox()
}
