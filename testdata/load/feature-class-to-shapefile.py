# Name: FeatureClassToShapefile_Example2.py
# Description: Use FeatureClassToShapefile to convert feature classes to shapefiles.

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inFeatures = ["climate.shp", "majorrds.shp"]
outLocation = "C:/output"
 
# Run FeatureClassToShapefile
arcpy.conversion.FeatureClassToShapefile(inFeatures, outLocation)