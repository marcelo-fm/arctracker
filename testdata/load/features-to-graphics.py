# Name: FeaturesToGraphics.py
# Description: Converts a polygon feature layer to polygon graphics.
# Requirements: None

# Import system models
import arcpy

# Set the workspace
arcpy.env.workspace = r"C:\data\input"

# Set local variables
out_layer = "NYBoroughs"
myquery = "AREATYPE = 'Borough'"

# Select the features to convert
in_layer = arcpy.management.SelectLayerByAttribute("NYCounties", 
                                                   "NEW_SELECTION", myquery)

# Run FeaturesToGraphics
arcpy.conversion.FeaturesToGraphics(in_layer, out_layer, "EXCLUDE_FEATURES")