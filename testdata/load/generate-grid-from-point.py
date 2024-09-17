# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Select the needed airport from airports layer
airports = "Airports"
whereClause = "airport_code = 'CLT'"
clt_layer = arcpy.SelectLayerByAttribute_management(airports,
                                                    "NEW_SELECTION",
                                                    whereClause)

# Create GRG
arcpy.GenerateGRGFromPoint_defense(clt_layer,"GenerateGRGFromPoint",
                                   10, 10, 1000, 1000,
                                   "METERS",
                                   "UPPER_LEFT",
                                   "ALPHA_NUMERIC",
                                   "-",
                                   0, "DEGREES")