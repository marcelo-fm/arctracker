#Delete Overviews with Query

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "remove.gdb/md2"
query = "#"
updatebnd = "#"
markovr = "#"
delovr = "DELETE_OVERVIEW_IMAGES"
delitemcache = "#"
removeitem = "NO_REMOVE_MOSAICDATASET_ITEMS"
updatecs = "UPDATE_CELL_SIZES"

arcpy.RemoveRastersFromMosaicDataset_management(
     mdname, query, updatebnd, markovr, delovr, delitemcache, 
     removeitem, updatecs)