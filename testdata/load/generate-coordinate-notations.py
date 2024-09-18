# Description: Add additional coordinate fields to data and then create points 
#              from output table.

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Add additional coordinate formats
in_coords = r"C:/CSV/TableToPoint.csv"
out_table = "TableWithMGRS"
arcpy.GenerateCoordinateNotations_defense(in_coords, out_table, "x", "DD_2", "y")

# Create points
result_point = "Output_Point"
arcpy.CoordinateTableToPoint_defense(out_table, result_point, "MGRS", "MGRS")