# Name: SetControlPointAtIntersect_standalone_script.py
# Description: Creates a control point at vertices that are shared by one or 
#              more line or polygon features. 

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
arcpy.env.cartographicPartitions = "partitions.lyrx"

# Set local variables
in_line_or_polygon_features = "parcels.lyrx"
in_features = "roads.lyrx"

# Execute Set Representation Control Point At Intersect
arcpy.SetControlPointAtIntersect_cartography(in_line_or_polygon_features, 
                                             in_features)