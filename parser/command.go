package parser

import (
	"strings"
	"unicode"

	"github.com/rs/zerolog/log"
)

// parseModule retorna o nome do módulo correto para a URL.
func parseModule(moduleName string) string {
	switch moduleName {
	case "management":
		return "data-management"
	case "edit":
		return "editing"
	case "ddd":
		return "3d-analyst"
	case "gapro":
		return "geoanalytics-desktop"
	case "md":
		return "multidimension"
	case "nd":
		return "network-diagram"
	case "na":
		return "network-analyst"
	case "stpm":
		return "space-time-pattern-mining"
	case "oi":
		return "oriented-imagery"
	case "transit":
		return "public-transit"
	case "rm":
		return "reality-mapping"
	case "ra":
		return "raster-analysis"
	case "agolservices":
		return "ready-to-use"
	case "stats":
		return "spatial-statistics"
	case "tn":
		return "trace-network"
	case "un":
		return "utility-networks"
	default:
		return moduleName
	}
}

// parseTool retorna o nome da ferramenta correto para a URL.
func parseTool(toolName string) string {
	switch toolName {
	case "EncloseMultiPatch":
		return "enclose-multipatch"
	case "Import3DFiles":
		return "import-3d-files"
	case "Intersect3D":
		return "intersect-3d-3d-analyst-"
	case "ArcGISProject":
		return ""
	case "CreateSpaceTimeCubeMDRasterLayer":
		return "createcubefrommdrasterlayer"
	case "EmergingHotSpotAnalysis":
		return "emerginghotspots"
	case "VisualizeSpaceTimeCube3D":
		return "visualizecube3d"
	case "VisualizeSpaceTimeCube2D":
		return "visualizecube2d"
	default:
		var tool string = strings.Clone(toolName)
		indexes := make([]int, 0, len(tool))
		for i, r := range toolName[1:] {
			if !unicode.IsUpper(r) {
				continue
			}
			if unicode.IsDigit(rune(toolName[i])) {
				log.Debug().
					Str("Tool", toolName).
					Int("CmdIndex", i).
					Str("Char", string(r)).
					Msgf("%s is a digit", string(toolName[i]))
				continue
			}
			log.Debug().
				Str("Tool", toolName).
				Int("CmdIndex", i).
				Str("Char", string(r)).
				Str("PreviousWords", toolName[:i+1]).
				Str("NextWords", toolName[i+1:]).
				Send()
			indexes = append(indexes, i+1)
		}
		if len(indexes) > 0 {
			var parts []string
			start := 0
			for _, index := range indexes {
				parts = append(parts, tool[start:index])
				start = index
			}
			parts = append(parts, tool[indexes[len(indexes)-1]:])

			tool = strings.Join(parts, "-")
		}
		return strings.ToLower(tool)
	}
}
