# Convert building footprints to points and number the points.

# Import modules
import arcpy

# Set workspace
arcpy.env.workspace = r"C:/Data.gdb"

# Get building center points
result_points = "Building_Points"
arcpy.management.FeatureToPoint("Buildings_1", result_points)

# Number the points that represent buildings
arcpy.defense.NumberFeatures(result_points,
                             "building_number",
                             None,
                             "CENTER",
                             "TEXT",
                             25,
                             5,
                             "center_bldg",
                             "ADD_DISTANCE")