# Description: Find highest point at an airport - can be a possible obstruction.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Select Charlotte airport area from airports layer
airports = "Airports"
whereClause = "airport_code = 'CLT'"
clt_layer = arcpy.management.SelectLayerByAttribute(airports,
                                                    "NEW_SELECTION",
                                                    whereClause)
# Inputs
input_surface = "n36.dt2"

# Find highest point in the Charlotte airport area
arcpy.defense.FindHighestLowestPoint(input_surface,
                                     "FindHighestPoint",
                                     "HIGHEST",
                                     clt_layer)