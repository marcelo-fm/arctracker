# Description: Create Linear Line of Sight to test siting of a radio antenna

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"

# Select antenna to test
antenna_layer = "antennas"
whereClause = "antenna_call_sign = 'KJT'"
test_ant_layer = arcpy.management.MakeFeatureLayer(antenna_layer, whereClause)

# Select observer test location
obs_layer = "observer_locations"
whereClause = "site_name = 'test_site'"
test_obs_layer = arcpy.management.MakeFeatureLayer(obs_layer, whereClause)

# Inputs
input_surface = "n36.dt2"

# Create line of sight between selected antenna and observer locations
arcpy.defense.LinearLineOfSight(test_obs_layer,
                                test_ant_layer,
                                input_surface,
                                "LineOfSight",
                                "SightLines",
                                "Test_Observers",
                                "Test_Targets",
                                None,
                                2,
                                0,
                                "NO_PROFILE_GRAPH")