# Name: FeatureVerticesToPoints_Example2.py
# Description: Use FeatureVerticesToPoints function to get the mid-points
#              of input line features

 
# import system modules 
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"
 
# Set local variables
inFeatures = "majorrds.shp"
outFeatureClass = "c:/output/output.gdb/majorrds_midpt"

# Execute FeatureVerticesToPoints
arcpy.FeatureVerticesToPoints_management(inFeatures, outFeatureClass, "MID")