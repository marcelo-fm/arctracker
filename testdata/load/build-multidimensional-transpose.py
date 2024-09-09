## import arcpy and set workspace

import arcpy
arcpy.env.workspace = "C:/Workspace/data"

## Build the transpose for a CRF of temperature data

arcpy.management.BuildMultidimensionalTranspose(
	"Temperature_CRF")