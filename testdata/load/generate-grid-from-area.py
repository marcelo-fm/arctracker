# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Select airport area
airports = "Airports"
whereClause = "airport_code = 'CLT'"
clt_layer = arcpy.SelectLayerByAttribute_management(airports,
                                                    "NEW_SELECTION",
                                                    whereClause)

# Create GRG
arcpy.GenerateGRGFromArea_defense(clt_layer,
                                  r"GenerateGRGFromArea",
                                  1000, 1000,
                                  "METERS",
                                  "UPPER_LEFT",
                                  "ALPHA_NUMERIC",
                                  "-")