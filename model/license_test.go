package model

import (
	"testing"
)

var expectedColumns [6]string = [6]string{
	"Title",
	"Command",
	"Basic",
	"Standard",
	"Advanced",
	"URL",
}

var expectedLicense License = License{
	Title:    "Buffer (Analysis)",
	Name:     "arcpy.analysis.Buffer",
	Basic:    "Limited",
	Standard: "Limited",
	Advanced: "Yes",
	URL:      "https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/buffer.htm",
}

func TestLicenseColumns(t *testing.T) {
	licenseColumns := LicenseColumns()
	for i, title := range expectedColumns {
		if licenseColumns[i].Title != title {
			t.Errorf("in %d Column, expected %s, got %s", i, title, licenseColumns[i].Title)
		}
	}
}

func TestCSVHeaders(t *testing.T) {
	cols := CSVHeaders()
	for i, title := range expectedColumns {
		if cols[i] != title {
			t.Errorf("in %d CSV Column, expected %s, got %s", i, title, cols[i])
		}
	}
}

func TestToRow(t *testing.T) {
	row := expectedLicense.ToRow()
	if row[0] != expectedLicense.Title {
		t.Errorf("expected %s, got %s", expectedLicense.Title, row[0])
	}
	if row[1] != expectedLicense.Name {
		t.Errorf("expected %s, got %s", expectedLicense.Name, row[1])
	}
	if row[2] != expectedLicense.Basic {
		t.Errorf("expected %s, got %s", expectedLicense.Basic, row[2])
	}
	if row[3] != expectedLicense.Standard {
		t.Errorf("expected %s, got %s", expectedLicense.Standard, row[3])
	}
	if row[4] != expectedLicense.Advanced {
		t.Errorf("expected %s, got %s", expectedLicense.Advanced, row[4])
	}
	if row[5] != expectedLicense.URL {
		t.Errorf("expected %s, got %s", expectedLicense.URL, row[5])
	}
}
