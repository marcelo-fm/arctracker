package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/internal/model"
)

func NewTable(licenses []model.License) *widget.Table {
	rows := make([][]string, len(licenses))
	for i, l := range licenses {
		rows[i] = l.ToRow()
	}
	tb := widget.NewTableWithHeaders(
		func() (int, int) {
			return len(licenses), 6
		},
		func() fyne.CanvasObject {
			return widget.NewLabel("template")
		},
		func(id widget.TableCellID, cell fyne.CanvasObject) {
			label := cell.(*widget.Label)
			label.SetText(rows[id.Row][id.Col])
		},
	)
	tb.SetColumnWidth(0, 300)
	tb.SetColumnWidth(1, 300)
	tb.SetColumnWidth(2, 200)
	tb.SetColumnWidth(3, 200)
	tb.SetColumnWidth(4, 200)
	tb.SetColumnWidth(5, 300)
	return tb
}
