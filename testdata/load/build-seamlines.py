# Build seamlines using the  NORTH_WEST sort method

import arcpy
arcpy.env.workspace = "C:/Workspace"

mdname = "Seamlines.gdb/md"
cellsize = "40"
sortmethod = "NORTH_WEST"
sortorder = "#"
orderattribute = "#"
orderbase = "#"
viewpnt = "#"
computemethod = "RADIOMETRY"
blendwidth = "5"
blendtype = "INSIDE"
requestsize = "#"

arcpy.BuildSeamlines_management(
    mdname, cellsize, sortmethod, sortorder, orderattribute, 
    orderbase, viewpnt, computemethod, blendwidth, blendtype, 
    requestsize)