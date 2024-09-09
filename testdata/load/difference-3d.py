'''****************************************************************************
Name: Difference3D Example
Description: This script demonstrates how to create
             shadow volumes that fall along a specified surface using the
             Difference3D tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
inMP = 'buildings.shp'
eraseMP = 'bldg_extensions.shp'
outMP = arcpy.CreateUniqueName('bldgs_without_extensions.shp')

# Execute Difference3D
arcpy.Difference3D_3d(inMP, eraseMP, outMP)