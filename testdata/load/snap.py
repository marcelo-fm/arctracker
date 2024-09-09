# Name: Snap.py
# Description: Snap climate regions boundary to vegetation layer boundary 
#              to ensure common boundary is coincident

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Make backup copy of climate regions feature class, since modification with 
# the Editing tools below is permanent
climate = "climate.shp"
climateBackup = "C:/output/Output.gdb/climateBackup"
arcpy.management.CopyFeatures(climate, climateBackup)

# Densify climate regions feature class to make sure there are enough vertices 
# to match detail of vegetation layer when layers are snapped
arcpy.edit.Densify(climate, "DISTANCE", "10 Feet")

# Snap climate regions feature class to  vegetation layer vertices and edge
veg = "Habitat_Analysis.gdb/vegtype"

# First, snap climate region vertices to the nearest vegetation layer vertex 
# within 30 Feet
snapEnv1 = [veg, "VERTEX", "30 Feet"]

# Second, snap climate region vertices to the nearest vegetation layer edge 
# within 20 Feet
snapEnv2 = [veg, "EDGE", "20 Feet"]
arcpy.edit.Snap(climate, [snapEnv1, snapEnv2])