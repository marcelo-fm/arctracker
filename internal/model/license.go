package model

import "github.com/charmbracelet/bubbles/table"

type License struct {
	Title    string `json:"title"`
	Name     string `json:"name"`
	Basic    string `json:"basic"`
	Standard string `json:"standard"`
	Advanced string `json:"advanced"`
	URL      string `json:"url"`
}

func LicenseColumns() []table.Column {
	return []table.Column{
		{Title: "Título", Width: 25},
		{Title: "Comando", Width: 20},
		{Title: "Basic", Width: 6},
		{Title: "Standard", Width: 6},
		{Title: "Advanced", Width: 6},
		{Title: "URL", Width: 20},
	}
}

func CSVHeaders() []string {
	return []string{
		"Título",
		"Comando",
		"Basic",
		"Standard",
		"Advanced",
		"URL",
	}
}

func (l *License) ToRow() []string {
	return []string{
		l.Title,
		l.Name,
		l.Basic,
		l.Standard,
		l.Advanced,
		l.URL,
	}
}

func (l *License) ToTableRow() table.Row {
	return table.Row(l.ToRow())
}
