# Name: FeatureToRaster_Ex_02.py
# Description: Converts features to a raster dataset.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inFeature = "roads.shp"
outRaster = "c:/output/roadsgrd"
cellSize = 25
field = "CLASS"

# Run FeatureToRaster
arcpy.conversion.FeatureToRaster(inFeature, field, outRaster, cellSize)