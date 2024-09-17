# Synchronize source and add new data

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "syncmd.gdb/mdnew"
query = "#"
updatenew = "UPDATE_WITH_NEW_ITEMS"
syncstale = "SYNC_STALE"
updatecs = "#"
updatebnd = "#"
updateovr = "#"
buildpy = "NO_PYRAMIDS"
calcstats = "NO_STATISTICS"
buildthumb = "NO_THUMBNAILS"
buildcache = "NO_ITEM_CACHE"
updateras = "NO_RASTER"
updatefield = "NO_FIELDS"
fields = "#"

arcpy.SynchronizeMosaicDataset_management(
    mdname, query, updatenew, syncstale, updatecs, updatebnd, 
    updateovr, buildpy, calcstats, buildthumb, buildcache,
    updateras, updatefield, fields)