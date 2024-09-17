# Calculate the Mininum Cell Size and Maximum Cell Size with default setting

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "cellsize.gdb/md"
query = "#"
calmin = "MIN_CELL_SIZES"
calmax = "MAX_CELL_SIZES"
maxfactor = "#"
tolerancefactor = "#"
updatemiss = "#"

arcpy.CalculateCellSizeRanges_management(
     mdname, query, calmin, calmax, maxfactor, tolerancefactor, updatemiss)