package gui

import (
	"fmt"
	"strings"

	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/lang"
	"fyne.io/fyne/v2/widget"
	"github.com/marcelo-fm/arctracker/internal/model"
)

func NewTable(licenses []model.License) *widget.Table {
	rows := make([][]string, len(licenses))
	headers := model.CSVHeaders()
	for i, l := range licenses {
		rows[i] = l.ToRow()
	}
	tb := widget.NewTableWithHeaders(
		func() (int, int) {
			return len(licenses), 6
		},
		func() fyne.CanvasObject {
			return container.NewHBox(widget.NewLabel(""), widget.NewHyperlink("", nil))
		},
		func(id widget.TableCellID, cell fyne.CanvasObject) {
			obj := cell.(*fyne.Container)
			switch id.Col {
			case 5:
				link := obj.Objects[1].(*widget.Hyperlink)
				link.SetText(rows[id.Row][0])
				link.SetURLFromString(rows[id.Row][id.Col])
			default:
				label := obj.Objects[0].(*widget.Label)
				label.SetText(rows[id.Row][id.Col])
				if id.Col >= 2 && id.Col <= 4 {
					label.TextStyle.Bold = strings.Contains(label.Text, "Yes")
				}
			}
		},
	)
	tb.SetColumnWidth(0, 300)
	tb.SetColumnWidth(1, 300)
	tb.SetColumnWidth(2, 200)
	tb.SetColumnWidth(3, 200)
	tb.SetColumnWidth(4, 200)
	tb.SetColumnWidth(5, 300)

	tb.CreateHeader = func() fyne.CanvasObject {
		return widget.NewLabel("0000000")
	}

	tb.UpdateHeader = func(id widget.TableCellID, o fyne.CanvasObject) {
		label := o.(*widget.Label)
		if id.Col == -1 {
			label.SetText(fmt.Sprint(id.Row))
			return
		}
		label.SetText(lang.L(headers[id.Col]))
	}

	return tb
}
