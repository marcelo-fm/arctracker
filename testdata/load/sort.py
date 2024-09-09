# Name: Sort_example2.py
# Description: Sorts wells by location and well yield.

# Import system modules
import arcpy

# Set workspace environment
arcpy.env.workspace = "C:/data/newfoundland.gdb"

# set local variables
in_dataset = "wells"
out_dataset = "wells_Sort"

# Order features first by location (Shape) and then by WELL_YIELD
sort_fields = [["Shape", "ASCENDING"], ["WELL_YIELD", "DESCENDING"]]

# Use Peano algorithm
sort_method = "PEANO"

# execute the function
arcpy.Sort_management(in_dataset, out_dataset, sort_fields, sort_method)