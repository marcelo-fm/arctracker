# Name: TableCompare.py
# Description: Compare two dBASE tables and return comparison result.

# import system modules 
import arcpy

# Set local variables
base_table= "C:/Workspace/wells.dbf"
test_table = "C:/Workspace/wells_new.dbf"
sort_field = "WELL_ID"
compare_type = "ALL"
ignore_option = "IGNORE_EXTENSION_PROPERTIES"
attribute_tolerance = "WELL_DEPTH 0.001"
omit_field = "#"
continue_compare = "CONTINUE_COMPARE"
compare_file = "C:/Workspace/well_compare.txt"

# Process: FeatureCompare
compare_result = arcpy.management.TableCompare(
    base_table, test_table, sort_field, compare_type, ignore_option, 
    attribute_tolerance, omit_field, continue_compare, compare_file)