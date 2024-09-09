# Name: MultipatchToRaster_Ex_02.py
# Description: Converts multipatch features to a raster dataset.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "c:/data"

# Set local variables
inFeatures = "buildings.shp"
outRaster = "c:/output/outbuildings.tif"
cellSize = 0.5

# Run MultipatchToRaster
arcpy.conversion.MultipatchToRaster(inFeatures, outRaster, cellSize)