//go:build !author
// +build !author

package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
)

func BottomInfo() *fyne.Container {
	return container.NewHBox()
}
