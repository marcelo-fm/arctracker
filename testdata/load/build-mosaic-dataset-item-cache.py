#Define mosaic dataset item cache without generating the cache file

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "itemcache.gdb/md"
query = "#"
definecache = "DEFINE_CACHE"
generatecache = "NO_GENERATE_CACHE"
cachepath = "C:/workspace/itemcache"
compression = "LOSSY"
compquality = "80"
maxrow = "#"
maxcolumn = "#"

arcpy.BuildMosaicDatasetItemCache_management(
     mdname, query, definecache, generatecache, cachepath, compression, 
     compquality, maxrow, maxcolumn)