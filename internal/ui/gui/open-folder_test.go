package gui_test

import (
	"testing"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/test"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/internal/ui/gui"
)

func TestNewOpenFolderDialog(t *testing.T) {
	folderTest := binding.NewString()
	w := test.NewWindow(nil)
	fod := gui.NewOpenFolderDialog(folderTest, w)
	fodContainer := fod.(*fyne.Container)
	btn := fodContainer.Objects[1].(*widget.Button)
	test.Tap(btn)
}
