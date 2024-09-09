# Name: CalculatePolygonMainAngle_standalone_script.py
# Description: Calculates the dominant angles of input polygon features and 
#              assigns the values to a specified field in the feature class

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "cartography.gdb/buildings_area"
angle_field = "poly_angle"
rotation_method = "ARITHMETIC"

# Execute Calculate Polygon Main Angle
arcpy.CalculatePolygonMainAngle_cartography(in_features, angle_field, 
                                            rotation_method)