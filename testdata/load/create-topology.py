# Name: CreateTopology_Example.py
# Description: Creates a new topology (these must reside within a feature dataset)

# Import system modules
import arcpy
 
arcpy.env.workspace = "h:/workspace"
arcpy.CreateTopology_management("d:/landuse.gdb/landuse", "landuse_Topology")