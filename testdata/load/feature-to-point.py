# Name: FeatureToPoint_Example2.py
# Description: Use FeatureToPoint function to find a point inside each park

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

#  Set local variables
inFeatures = "parks.shp"
outFeatureClass = "c:/output/output.gdb/parks_pt"

# Use FeatureToPoint function to find a point inside each park
arcpy.management.FeatureToPoint(inFeatures, outFeatureClass, "INSIDE")