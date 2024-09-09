# Description: Rename a file geodatabase feature class

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/workspace/test.gdb"

# Set local variables
in_data =  "test"
out_data = "testFC"
data_type = "FeatureClass"

# Run Rename
arcpy.management.Rename(in_data, out_data, data_type)