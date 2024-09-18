##===========================
##Compute Dirty Area
##Usage: ComputeDirtyArea_management in_mosaic_dataset {where_clause} timestamp
##                                   out_feature_class

import arcpy
arcpy.env.workspace = "c:/workspace"

# Find the area changed after 6:00pm Jan 12th 2010
arcpy.ComputeDirtyArea_management("fgdb.gdb/md", "#", "2010-01-12T18:00:00.00-08:00", "dirtyarea.shp")