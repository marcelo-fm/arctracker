# Description: Create Radial Line of Sight and Range to test siting of an antenna 
# antennas

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"

# Select antenna to test
antenna_layer = "antennas"
whereClause = "antenna_call_sign = 'KJT'"
test_ant_layer = arcpy.management.MakeFeatureLayer(antenna_layer, whereClause)

# Inputs
input_surface = "n36.dt2"

# Create radial line of sight for antennas
arcpy.defense.RadialLineOfSightAndRange(test_obs_layer, input_surface, 
                                        "Viewshed", "FieldOfView", "Range", 
                                        2, 1000, 3000, 0, 360)