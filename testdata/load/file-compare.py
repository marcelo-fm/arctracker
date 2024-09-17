# Name: FileCompare.py
# Description: Compare two text files and return comparison result.

# import system modules 
import arcpy

# Set local variables
base_file= "C:/Workspace/well_xycoordinates.txt"
test_file= "C:/Workspace/new_well_coordinates.txt"
file_type = "ASCII"
continue_compare = "CONTINUE_COMPARE"
compare_file = "C:/Workspace/well_file_compare.txt"

# Process: FeatureCompare
compare_result = arcpy.FileCompare_management(base_file, test_features, 
                                              file_type, continue_compare, 
                                              compare_file)
print(compare_result)
print(arcpy.GetMessages())