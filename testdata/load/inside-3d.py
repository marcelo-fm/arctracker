'''****************************************************************************
Name: Inside3D Example
Description: This script demonstrates how to use the
             Inside3D tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inFC = 'Points_3D.shp' # the input feature
inMP = 'Buildings.shp' # the input multi-patch

# Ensure output has a unique name
outTbl = arcpy.CreateUniqueName('Output_Table.dbf')

# Execute Inside 3D
arcpy.Inside3D_3d(inFC, inMP, outTbl)