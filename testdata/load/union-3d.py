'''****************************************************************************
Name: Union3D Example
Description: This script demonstrates how to use the 
             Union3D tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inMP = "multipatch.shp"

# Ensure output multipatch has a unique name
outMP = arcpy.CreateUniqueName("union_output.shp")
outTbl = arcpy.CreateUniqueName("UnionTable.dbf")
GroupField = "Type"
optimize = "DISABLE"
solids = "ENABLE"

# Execute Union3D
arcpy.ddd.Union3D(inMP, outMP, GroupField, optimize, solids, outTbl)