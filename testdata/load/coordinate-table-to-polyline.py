# Description: Create polylines from tabular data and find a representative 
#              center point of each line.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Create polylines
input_table = r"C:/CSV/TableToPolyline.csv"
result_line = "Output_Polyline"
arcpy.CoordinateTableToPolyline_defense(input_table, result_line, "POINT_X", 
                                        "DD_2", "POINT_Y", "Group_")

# Find representative center point
result_center = "Output_Centers"
arcpy.FeatureToPoint_management(result_line, result_center)