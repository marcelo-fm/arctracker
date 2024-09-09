import arcpy
 
# Set a default workspace
arcpy.env.workspace = "c:/data"
 
# Remove two indexes from the feature class
arcpy.management.RemoveIndex("/county.gdb/lots", ["indexa", "indexb"])