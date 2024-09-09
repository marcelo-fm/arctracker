# Name: CreateThiessenPolygons_Example2.py
# Description: Creates Thiessen polygons
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/data.gdb"
 
# Set local variables
inFeatures = "schools"
outFeatureClass = "c:/output/output.gdb/thiessen1"
outFields = "ALL"
 
# Run CreateThiessenPolygons
arcpy.analysis.CreateThiessenPolygons(inFeatures, outFeatureClass, outFields)