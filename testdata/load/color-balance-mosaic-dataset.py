# Color Correction Mosaic Dataset with block field

import arcpy
arcpy.env.workspace = "C:/workspace"

mdname = "CC.gdb/cc2"
ccmethod = "HISTOGRAM"
dogesurface = "#"
targetras = "#"
excluderas = "#"
prestretch = "NONE"
gamma = "#"
blockfield = "BLOCKNAME"

arcpy.ColorBalanceMosaicDataset_management(
     mdname, ccmethod, dogesurface, targetras, excluderas, 
     prestretch, gamma, blockfield)