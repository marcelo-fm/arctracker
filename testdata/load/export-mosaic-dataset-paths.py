#Export broken raster path in FGDB Mosaic Dataset to dbf table

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "exportmd.gdb/md"
outtable = "C:/workspace/brokenpaths.dbf"
query = "#"
mode = "BROKEN"
pathtype = "RASTER"

arcpy.ExportMosaicDatasetPaths_management(mdname, outtable, query, 
                                          mode, pathtype)