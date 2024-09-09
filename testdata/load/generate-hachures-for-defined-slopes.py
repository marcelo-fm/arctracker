""" Name: GenerateHachuresForDefinedSlopes_standalone_script.py
    Description: Generates multipart polygons representing
                 the slope between the lines of an upper and lower slope 
	
"""

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/Data/Hachures.gdb"

# Set local variables
upper_lines = "UpperEdges"
lower_lines = "LowerEdges"
output_type = "POLYGON_TRIANGLES"
output_feature_class = "Hachures_output"
fully_connected = "NOT_CONNECTED"
search_distance = "20 Meters"
interval = "10 Meters"
minimum_length = "0 Meters"
alternate_hachures = "UNIFORM_HACHURES"
perpendicular = False
polygon_base_width = "5 Meters"

# Execute Generate Hachures For Defined Slopes
arcpy.cartography.GenerateHachuresForDefinedSlopes(upper_lines,
                                                   lower_lines,
                                                   output_feature_class,
                                                   output_type,
                                                   fully_connected,
                                                   search_distance,
                                                   interval,
                                                   minimum_length,
                                                   alternate_hachures,
                                                   perpendicular,
                                                   polygon_base_width)