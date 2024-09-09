'''****************************************************************************
Name: Detect Periods of Activity
Description: 
****************************************************************************'''
# Import system modules
import arcpy
import tempfile
import math

in_features = arcpy.GetParameterAsText(0)
out_volume = arcpy.GetParameterAsText(1)
grouping_field = arcpy.GetParameterAsText(2)


try:
    arcpy.MinimumBoundingVolume_3d(in_features, 'Shape.Z', out_volume, 
                                   'CONCAVE_HULL','LIST', group_field)

except arcpy.ExecuteError:
    print(arcpy.GetMessages())