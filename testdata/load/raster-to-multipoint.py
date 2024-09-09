'''*********************************************************************
Name: RasterToMultipoint Example
Description: This script demonstrates how to use
             the RasterToMultipoint tool to create multipoint datasets
             fot all IMG rasters in a target workspace.
**********************************************************************'''
# Import system modules
import arcpy

# Set default workspace
arcpy.env.workspace = "C:/data"
# Create the list of IMG rasters
rasterList = arcpy.ListRasters("*", "IMG")
# Loop the process for each raster
if rasterList:
    for raster in rasterList:
        # Set Local Variables
        # [:-4] strips the last 4 characters (.img) from the raster name
        outTbl = "VIP_" + raster[:-4] + ".dbf"
        method = "VIP_HISTOGRAM"
        zfactor = 1
        #Execute RasterToMultipoint
        arcpy.ddd.RasterToMultipoint(raster, "",outTbl, method, "", zfactor)
else:
    print("There are no IMG rasters in the " + env.workspace + " directory.")