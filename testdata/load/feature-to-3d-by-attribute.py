'''****************************************************************************
Name: FeatureTo3DByAttribute Example
Description: This script demonstrates how to use the
             FeatureTo3DByAttribute tool.
****************************************************************************'''
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data'

# Set Local Variables
InFC = 'Points_2D.shp'
Height_Field = 'POPULATION'

# Ensure output has unique name
OutFC = arcpy.CreateUniqueName('Points_3D.shp')

# Execute ConstructSightLines
arcpy.FeatureTo3DByAttribute_3d(InFC, OutFC, Height_Field)