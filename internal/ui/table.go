package ui

import (
	"fmt"
	"os"

	"github.com/charmbracelet/bubbles/table"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

var baseStyle = lipgloss.NewStyle().
	BorderStyle(lipgloss.NormalBorder()).
	BorderForeground(lipgloss.Color("240"))

type model struct {
	table table.Model
}

func New(columns []table.Column, rows []table.Row) *Table {
	t := table.New(
		table.WithColumns(columns),
		table.WithRows(rows),
		table.WithFocused(true),
		table.WithHeight(10),
	)

	s := table.DefaultStyles()
	s.Header = s.Header.
		BorderStyle(lipgloss.NormalBorder()).
		BorderForeground(lipgloss.Color("240")).
		BorderBottom(true).
		Bold(false)
	s.Selected = s.Selected.
		Foreground(lipgloss.Color("229")).
		Background(lipgloss.Color("#00619b")).
		Bold(false)
	t.SetStyles(s)

	m := model{t}
	return &Table{m}
}

type Table struct {
	m model
}

func (m model) Init() tea.Cmd { return nil }

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	var cmd tea.Cmd
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "esc":
			if m.table.Focused() {
				m.table.Blur()
			} else {
				m.table.Focus()
			}
		case "q", "ctrl+c":
			return m, tea.Quit
		case "enter":
			columns := m.table.Columns()
			row := m.table.SelectedRow()
			return m, tea.Batch(
				tea.Printf(
					"%s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n%s: %s\n",
					row[0],
					columns[1].Title,
					row[1],
					columns[2].Title,
					row[2],
					columns[3].Title,
					row[3],
					columns[4].Title,
					row[4],
					columns[5].Title,
					row[5],
				),
			)
		}
	}
	m.table, cmd = m.table.Update(msg)
	return m, cmd
}

func (m model) View() string {
	return baseStyle.Render(m.table.View()) + "\n  " + m.table.HelpView() + "\n"
}

func (tb *Table) Run() {
	if _, err := tea.NewProgram(tb.m).Run(); err != nil {
		fmt.Println("Error running program:", err)
		os.Exit(1)
	}
}
