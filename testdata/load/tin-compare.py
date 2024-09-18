# Description: Compare two TINs and return comparison result.

# import system modules 
import arcpy

# Set local variables
base_tin= "C:/Workspace/basetin"
test_tin= "C:/Workspace/newtin"
compare_type = "ALL"
continue_compare = "CONTINUE_COMPARE"
compare_file = "C:/Workspace/tincompare.txt"

compare_result = arcpy.TINCompare_management(base_tin, test_tin, compare_type, 
                                             continue_compare, compare_file)
print(compare_result)
print(arcpy.GetMessages())