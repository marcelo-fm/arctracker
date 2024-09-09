# Description: Convert point features into line features

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/points.gdb"

# Set local variables
inFeatures = "in_points"
outFeatures = "out_lines"
lineField = "lineID"
sortField = "stopID"
transFields = ["OBJECTID", "stopID"]

# Run PointsToLine 
arcpy.management.PointsToLine(inFeatures, outFeatures, lineField, sortField,
                              "NO_CLOSE", "TWO_POINT", "BOTH_ENDS", transFields)