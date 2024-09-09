package parser

import (
	"strings"
	"unicode"
)

// parseModule retorna o nome do módulo correto para a URL.
func parseModule(module string) string {
	switch module {
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
	case "oi":
		return "oriented-imagery"
	case "transit":
		return "public-transit"
	case "rm":
		return "reality-mapping"
	case "stats":
		return "spatial-statistics"
	case "tn":
		return "trace-network"
	case "un":
		return "utility-networks"
	default:
		return module
	}
}

// parseTool retorna o nome da ferramenta correto para a URL.
func parseTool(toolName string) string {
	switch toolName {
	case "EncloseMultiPatch":
		return "enclose-multipatch"
	}
	var tool string = strings.Clone(toolName)
	for i, r := range toolName[1:] {
		if !unicode.IsUpper(r) {
			continue
		}
		tool = tool[:i+1] + "-" + tool[i+1:]
	}
	return strings.ToLower(tool)
}
