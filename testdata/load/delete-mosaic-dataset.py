#Delete mosaic dataset including the overview images

import arcpy
arcpy.env.workspace = "C:/Workspace"

mosaicds = "fileGDB.gdb/md2delete"
delOvr = "DELETE_OVERVIEW_IMAGES"
delCache = "NO_DELETE_ITEM_CACHE"

    
arcpy.DeleteMosaicDataset_management(mosaicds, delOvr, delCache)