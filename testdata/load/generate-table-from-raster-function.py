#====================================
# GenerateTableFromRasterFunction
# Usage:
# arcpy.management.GenerateTableFromRasterFunction(
#     raster_function, out_table, { {Name} {Value}; {Name} {Value}...}))
# arcpy.management.GenerateTableFromRasterFunction(
#     raster_function, out_table, {raster_function_arguments})

import arcpy

rasterfunc = "C:/Workspace/funcs/TestGeometry.rft.xml"
outfc = "C:/Workspace/polygonfeat.shp"
funcargs = "Raster C:/Workspace/data/testgeo.tif"

# Generate polygon feature class using custom python raster function
arcpy.management.GenerateTableFromRasterFunction(
rasterfunc, outfc, funcargs)