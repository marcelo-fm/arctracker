# Name: CopyFeatures_Example2.py
# Description: Convert all shapefiles in a folder to geodatabase feature classes
 
# Import system modules
import arcpy
import os
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
out_workspace = "c:/output/output.gdb"
 
# Use ListFeatureClasses to generate a list of shapefiles in the workspace 
# shown above.
fc_list = arcpy.ListFeatureClasses()
 
# Run CopyFeatures for each input shapefile
for shapefile in fc_list:
    # Determine the new output feature class path and name
    out_featureclass = os.path.join(out_workspace, 
                                    os.path.splitext(shapefile)[0])
    arcpy.management.CopyFeatures(shapefile, out_featureclass)