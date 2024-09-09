# Name: ConvertControlPointsToVertices_standalone_script.py
# Description: Converts control points on a line or 
#              polygon layer into vertices.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
in_layer = "roads.lyrx"

# Execute Convert Control Points To Vertices
arcpy.cartography.ConvertControlPointsToVertices(in_layer)