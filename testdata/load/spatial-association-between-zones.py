# Calculate the association between forest type and soil drainage class rasters.  

import arcpy 

# Set the current workspace
arcpy.env.workspace = r"c:\data\project_data.gdb"
arcpy.env.overwriteOutput = True

# Determine the association.
result = arcpy.stats.SpatialAssociationBetweenZones("forest_type", "Class_Name", 
               "soil_drainage", "ClassName", None, "forest_soil")

# Print the derived output for the Global Measure of Spatial Association.
globalV = result[4]
if globalV > 0.9:
    print('Forest type and soil drainage class are highly associated.')