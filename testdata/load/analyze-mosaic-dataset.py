#Analyze Mosaic Dataset with query definition
#Analyze all components of mosaic dataset

import arcpy
arcpy.env.workspace = "C:/Workspace"


mdname = "analyzemd.gdb/mosaicds"
query = "SensorName = 'Landsat-7-ETM+'"
checks = "FOOTPRINT;FUNCTION;RASTER;PATHS;STALE;PYRAMIDS;PERFORMANCE"

arcpy.AnalyzeMosaicDataset_management(mdname, query, checks)