'''******************************************************************
Name: AddZInformation Example
Description: This script demonstrates AddZInformation on all 
             z-aware features in a target workspace.
******************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'
# Create list of feature classes
fcList = arcpy.ListFeatureClasses()
if fcList:
    for fc in fcList:
        desc = arcpy.Describe(fc)
        if desc.hasZ:
            # Set Local Variables
            noise = 'No_Filter'
            if desc.shapeType == 'Polygon':
                Prop = ['Z_MIN', 'Z_MAX', 'VERTEX_COUNT']
            elif desc.shapeType == 'Point':
                Prop = 'Z'
            elif desc.shapeType == 'Multipoint':
                Prop = ['Z_MIN', 'Z_MAX', 'Z_MEAN']
            elif desc.shapeType == 'Polyline':
                Prop = 'LENGTH_3D'
            print('Completed adding Z information.')
            # Execute AddZInformation
            arcpy.ddd.AddZInformation(inFC, Prop, noise)