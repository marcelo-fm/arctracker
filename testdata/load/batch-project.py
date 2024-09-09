# Name: BatchProject.py
# Description: Changes coordinate systems of several datasets in a batch.

import arcpy

# Set workspace environment
arcpy.env.workspace = "C:/data/wgs1972.gdb"

# Input feature classes
input_features = ["cities", "counties", "blocks", "crime"]

# Output workspace
out_workspace = "C:/data/output.gdb"

# Output coordinate system - leave it empty
out_cs = ''

# Template dataset - it has GCS_WGS_1984 coordinate system
template = "C:/data/wgs1984.gdb/stateparks"

# Geographic transformation - 
transformation = "WGS_1972_To_WGS_1984_1"

res = arcpy.BatchProject(input_features, out_workspace, out_cs, template, transformation)