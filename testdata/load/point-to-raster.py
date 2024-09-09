# Name: PointToRaster_Ex_02.py
# Description: Converts point features to a raster dataset.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inFeatures = "ca_ozone_pts.shp"
valField = "ELEVATION"
outRaster = "c:/output/ca_elev02"
assignmentType = "MAXIMUM"
priorityField = ""
cellSize = 2000

# Run PointToRaster
arcpy.conversion.PointToRaster(inFeatures, valField, outRaster, 
                               assignmentType, priorityField, cellSize)