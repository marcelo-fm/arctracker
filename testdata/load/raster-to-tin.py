'''*********************************************************************
Name: RasterTin Example
Description: This script demonstrates how to use the 
             RasterTin tool to create a TIN for each IMG raster in the 
             target workspace.
**********************************************************************'''

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Create the list of IMG rasters
rasterList = arcpy.ListRasters("*", "IMG")
# Loop the process for each raster
if rasterList:
    for raster in rasterList:
        # Set Local Variables
        zTol = 2
        maxPts = 1500000
        zFactor = 1
        # [:-4] strips the last 4 characters (.img) from the raster name
        outTin = "C:/Output/TIN_" + raster[:-4] 
        print("Creating TIN from " + raster + ".")
        #Execute RasterTin
        arcpy.ddd.RasterTin(raster, outTIN, zTol, maxPts, zFactor)
    print("Finished.")
else:
    print("There are no IMG rasters in the " + env.workspace + " directory.")