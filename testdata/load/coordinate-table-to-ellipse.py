# Description: Create ellipses from tabular data and create a single feature 
#              representing area coverage of ellipses.

# Import system modules
import arcpy

# Set environment setting
sarcpy.env.workspace = r"C:/Data.gdb"
arcpy.env.overwriteOutput = True

# Create ellipses
input_table = r"C:/CSV/TableToEllipse.csv"
result_ellipse = "Output_Ellipse"
arcpy.CoordinateTableToEllipse_defense(input_table,
                                       result_ellipse, 
                                       "x",
                                       "Major",
                                       "Minor",
                                       "DD_2",
                                       "KILOMETERS",
                                       "y",
                                       "Orient",
                                       "DEGREES")

# Union resulting ellipses
result_union = "Output_Union"
arcpy.Union_analysis(result_ellipse, result_union)

# Dissolve polygons into one feature
result_dissolve = "Output_Dissolve"
arcpy.Dissolve_management(result_union, result_dissolve)