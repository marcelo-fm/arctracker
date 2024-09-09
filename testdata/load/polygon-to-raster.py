# Name: PolygonToRaster_Ex_02.py
# Description: Converts polygon features to a raster dataset.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inFeatures = "ca_counties.shp"
valField = "NAME"
outRaster = "c:/output/ca_counties"
assignmentType = "MAXIMUM_AREA"
priorityField = "MALES"
cellSize = 0.5

# Run PolygonToRaster
arcpy.conversion.PolygonToRaster(inFeatures, valField, outRaster, 
                                 assignmentType, priorityField, cellSize)