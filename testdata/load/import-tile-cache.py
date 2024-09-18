#Import tile cache for some levels from a pre-existing tile cache

import arcpy

    
cacheTarget = "C:/Data/CacheDatasets/Target"
cacheSource = "C:/Data/CacheDatasets/Source"
scales = "4000;2000;1000"
areaofinterest = "#"
overwrite = "MERGE"

arcpy.ImportTileCache_management(cacheTarget, cacheSource, scales, 
                                 areaofinterest, overwrite)