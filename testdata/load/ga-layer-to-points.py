# Name: GALayerToPoints_Example_02.py
# Description: Exports a geostatistical layer to points.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"
inPoints = "C:/gapyexamples/data/obs_pts.shp"
zField = ""
outPoints = "C:/gapyexamples/output/krig_pts"

# Execute GALayerToPoints
arcpy.GALayerToPoints_ga(inLayer, inPoints, zField, outPoints)