# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Select Charlotte airport from airports layer
airports = "Airports"
whereClause = "airport_code = 'CLT'"
clt_layer = arcpy.management.SelectLayerByAttribute(airports,
                                                    "NEW_SELECTION",
                                                    whereClause)

# Create GRG
arcpy.defense.GenerateReferenceSystemGRGFromArea(clt_layer,
                                                 "GenerateGRGFromArea",
                                                 "MGRS",
                                                 "GRID_ZONE_DESIGNATOR",
                                                 "NO_LARGE_GRIDS")