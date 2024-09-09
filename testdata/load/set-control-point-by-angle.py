# Name: SetControlPointByAngle_standalone_script.py
# Description: Places a control point at vertices along a line or polygon
#              outline where the angle created by a change in line direction is
#              less than or equal to a specified maximum angle

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
in_layer = "trails.lyrx"
minimum_angle_deviation = "135"

# Execute Set Representation Control Point At Intersect
arcpy.SetControlPointByAngle_cartography(in_layer, minimum_angle_deviation)