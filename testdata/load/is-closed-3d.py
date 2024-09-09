'''****************************************************************************
Name: IsClosed3D Example
Description: This script demonstrates how to use the
             IsClosed3D tool on all multipatches in a target workspace.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'
# Set Local Variables
for fc in arcpy.ListFeatureClasses(): # list features in workspace
    # Determine which features are multipatches
    if arcpy.Describe(fc).shapeType == 'MultiPatch':
        # Execute Is Closed 3D
        arcpy.IsClosed3D_3d(fc)