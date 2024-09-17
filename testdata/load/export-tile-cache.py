#Export tile cache for some levels to an EXPLODED format in 
#another location

import arcpy

    
cacheSource = "C:/Data/CacheDatasets/Source"
cacheTarget = "C:/Data/CacheDatasets"
cacheName = "Target"
cacheType = "TILE_CACHE"
storageFormat = "EXPLODED"
scales = "4000;2000;1000"
areaofinterest = "#"

arcpy.ExportTileCache_management(cacheSource, cacheTarget, cacheName,
     cacheType, storageFormat, scales, areaofinterest)