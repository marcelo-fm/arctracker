'''****************************************************************************
Name: Intersect3D Example
Description: This script demonstrates how to use the
             Intersect3D tool
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inMP1 = 'Boston_MP_Small.shp'
inMP2 = 'Boston_MP.shp'

# Ensure output has a unique name
outMP = arcpy.CreateUniqueName('Intersect.shp')

# Execute Intersect 3D
arcpy.Intersect3D_3d(inMP1, outMP, inMP2)