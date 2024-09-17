#compute tie points

import arcpy
arcpy.env.workspace = "c:/workspace"

#Compute tie points for a mosaic dataset
mdName = "BD.gdb/redlandsQB"
out_tiePoint = "BD.gdb/redlandsQB_tiePoints"

arcpy.ComputeTiePoints_rm(mdName, out_tiePoint, "MEDIUM")