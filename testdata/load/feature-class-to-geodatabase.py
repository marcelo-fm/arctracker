# Name: FeatureClassToGeodatabase_Example2.py
# Description: Use FeatureClassToGeodatabase to copy feature classes
#              to geodatabase format
 
# Import modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = 'C:/data'
 
# Set local variables
in_features = ['climate.shp', 'majorrds.shp']
out_location = 'C:/output/output.gdb'
 
# Run FeatureClassToGeodatabase
arcpy.conversion.FeatureClassToGeodatabase(in_features, out_location)