package assets

import (
	"embed"

	"fyne.io/fyne/v2"
)

//go:embed translation
var Translations embed.FS

//go:embed arctracker-logo-dark.png
var LogoContentDark []byte

//go:embed arctracker-logo-light.png
var LogoContentLight []byte

//go:embed icons/moon.png
var IconContentDark []byte

//go:embed icons/sun.png
var IconContentLight []byte

var LogoDark, LogoLight, IconDark, IconLight fyne.Resource

func init() {
	LogoDark = fyne.NewStaticResource("logo-dark", LogoContentDark)
	LogoLight = fyne.NewStaticResource("logo-light", LogoContentLight)
	IconDark = fyne.NewStaticResource("icon-dark", IconContentDark)
	IconLight = fyne.NewStaticResource("icon-light", IconContentLight)
}
