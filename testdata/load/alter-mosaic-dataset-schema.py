#Alter Mosaic Dataset Schema mainly works on SDE mosaic datasets. The 
#selected side tables of mosaic dataset will be created. If there are
#raster type settings, metadata fields will be create for that raster type.

import arcpy
arcpy.env.workspace = "C:/Workspace"
    
mosaicds = "sdeserver.sde/mosaicds"
ops = "ANALYSIS;BOUNDARY;LEVELS;LOG;OVERVIEW"
rastypes = "QuickBird;IKONOS;Match-AT"

arcpy.AlterMosaicDatasetSchema_management(mosaicds, ops, rastypes)