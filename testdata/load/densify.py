# Name: Snap.py
# Description: Snap climate regions boundary to vegetation layer
#              boundary to ensure common boundary is coincident

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Make backup copy of climate regions feature class, 
# since modification with the Editing tools below is permanent.
climateBackup = "backups/climate.shp"
arcpy.management.CopyFeatures('climate.shp', climateBackup)

# Densify climate regions feature class to make sure there are enough 
# vertices to match detail of vegetation layer when layers are snapped.
arcpy.edit.Densify('climate.shp', "DISTANCE", "10 Feet") 

# Snap climate regions feature class to vegetation layer vertices and 
# edge. First, snap climate region vertices to the nearest vegetation 
# vertex within 30 Feet. Second, snap climate region vertices to the 
# nearest vegetation edge within 20 Feet.
snapEnv1 = ["Habitat_Analysis.gdb/vegtype", "VERTEX", "30 Feet"]    
snapEnv2 = ["Habitat_Analysis.gdb/vegtype", "EDGE", "20 Feet"]       
arcpy.edit.Snap('climate.shp', [snapEnv1, snapEnv2])