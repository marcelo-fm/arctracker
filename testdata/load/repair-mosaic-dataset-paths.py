#Repair mosaic dataset paths

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "repairmd.gdb/md"
paths = "e:/temp/data c:/storage/mddata/e;d:/temp/data c:/storage/mddata/d"
query = "#"

arcpy.RepairMosaicDatasetPaths_management(mdname, paths, query)