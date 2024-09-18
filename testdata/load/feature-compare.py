# Name: FeatureCompare.py
# Description: Compare two feature classes and return comparison result.

# import system modules 
import arcpy

# Set local variables
base_features = "C:/Workspace/baseroads.shp"
test_features = "C:/Workspace/newroads.shp"
sort_field = "ROAD_ID"
compare_type = "ALL"
ignore_option = "IGNORE_M;IGNORE_Z"
xy_tolerance = "0.001 METERS"
m_tolerance = 0
z_tolerance = 0
attribute_tolerance = "Shape_Length 0.001"
omit_field = "#"
continue_compare = "CONTINUE_COMPARE"
compare_file = "C:/Workspace/roadcompare.txt"
 
# Process: FeatureCompare
compare_result = arcpy.FeatureCompare_management(
    base_features, test_features, sort_field, compare_type, ignore_option, 
    xy_tolerance, m_tolerance, z_tolerance, attribute_tolerance, omit_field, 
    continue_compare, compare_file)
print(compare_result[1])
print(arcpy.GetMessages())