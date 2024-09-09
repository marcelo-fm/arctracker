# Name: PolylineToRaster_Ex_02.py
# Description: Converts polyline features to a raster dataset.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inFeatures = "roads.shp"
valField = "CLASS"
outRaster = "c:/output/roads.tif"
assignmentType = "MAXIMUM_COMBINED_LENGTH"
priorityField = "LENGTH"
cellSize = 30

# Run PolylineToRaster
arcpy.conversion.PolylineToRaster(inFeatures, valField, outRaster, 
                                  assignmentType, priorityField, cellSize)