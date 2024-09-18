# Description: Create points from tabular data and create buffers around them.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Create points
input_table = r"C:/CSV/TableToPoint.csv"
result_point = "Output_Point"
arcpy.CoordinateTableToPoint_defense(input_table, result_point, "x", "DD_2", "y")

# Create buffers
result_buffer = "Output_Buffer"
arcpy.Buffer_analysis(result_point, result_buffer, "50 Meters")