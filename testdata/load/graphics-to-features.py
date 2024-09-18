# Name: GraphicsToFeatures.py
# Description: Converts a point graphics layer to a feature class and adds x,y 
# coordinate data to its attributes.
# Requirements: None

import arcpy

# Set environment
arcpy.env.workspace = r"C:\Data"

# Set local variables
in_layer = "graphics_coord.lyrx"
out_path = "Default.gdb"
geometry_type = "POINT"
result = arcpy.management.CreateFeatureclass(out_path, "out_fc", geometry_type)

# Execute the conversion
arcpy.conversion.GraphicsToFeatures(in_layer, 'POINT', result, 'DELETE_GRAPHICS')

# Add x,y coordinates to the new feature class
arcpy.management.AddXY("out_fc")