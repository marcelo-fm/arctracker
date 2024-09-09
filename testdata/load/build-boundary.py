# Build boundary only for the Quickbird data

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "boundary.gdb/md"
query = "SensorName = 'QuickBird'"
mode = "OVERWRITE"
simplify = "#"

arcpy.BuildBoundary_management(mdname, query, mode, simplify)