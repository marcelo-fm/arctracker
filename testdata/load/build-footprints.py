# Build Footprint by setting the valid pixel value range from 1 to 254
# Allow 25 vertices to be used to draw a single footprint polygon
# Skip the overviews image
# Build new boundary afterwards
# Build footprints based on minimum bounding geometry

import arcpy
arcpy.env.workspace = "C:/Workspace"

    
mdname = "Footprints.gdb/md"
query = "#"
method = "RADIOMETRY"
minval = "1"
maxval = "254"
nvertice = "25"
shrinkdis = "0"
maintainedge = "#"
skipovr = "SKIP_DERIVED_IMAGES"
updatebnd = "UPDATE_BOUNDARY"
requestsize = "#"
minregsize = "#"
simplify = "#"

arcpy.BuildFootprints_management(
     mdname, query, method, minval, maxval, nvertice, shrinkdis,
     maintainedge, skipovr, updatebnd, requestsize, minregsize, 
     simplify)