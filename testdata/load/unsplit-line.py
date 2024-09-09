# Name: UnsplitLine_Example2.py
# Description: Unsplit line features based on common attributes
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/Portland.gdb/Streets"
 
# Set local variables
inFeatures = "streets"
outFeatureClass = "C:/output/output.gdb/streets_unsplit"
dissolveFields = ["STREETNAME", "PREFIX"]
 
# Run UnsplitLine using STREETNAME and PREFIX as Dissolve Fields
arcpy.management.UnsplitLine(inFeatures, outFeatureClass, dissolveFields)