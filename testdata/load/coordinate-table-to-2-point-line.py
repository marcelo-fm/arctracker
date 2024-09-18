# Description: Densify line features created from tabular data

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Create lines
input_table = r"C:/CSV/TableTo2PointLine.csv"
result_line = "TableTo2Point"
arcpy.CoordinateTableTo2PointLine_defense(input_table, result_line, "POINT_X", 
                                          "POINT_X2", "DD_2", "POINT_Y", 
                                          "POINT_Y2")

# Densify lines
arcpy.Densify_edit(result_line, "DISTANCE", "2 Kilometers")