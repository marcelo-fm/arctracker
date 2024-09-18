# Description: Find the highest peak in Crowders State Park.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"

# Select state park
state_parks = "NCStateParks"
whereClause = "st_park_name = 'Crowders Mountain State Park'"
aoi_layer = arcpy.management.SelectLayerByAttribute(state_parks,
                                                    "NEW_SELECTION",
                                                    whereClause)

# Inputs
input_surface = "n36.dt2"

# Find highest peak 
arcpy.defense.FindLocalPeaksValleys(input_surface,
                                    "PeaksCrowdersMtn",
                                    "PEAKS",
                                    10,
                                    aoi_layer)