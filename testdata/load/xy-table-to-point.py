# XYTableToPoint.py
# Description: Creates a point feature class from input table

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = r"c:\output.gdb"

# Set the local variables
in_table = r"c:\data\tree.csv"
out_feature_class = "tree_points"
x_coords = "longitude"
y_coords = "latitude"
z_coords = "elevation"

# Make the XY event layer...
arcpy.management.XYTableToPoint(in_table, out_feature_class,
                                x_coords, y_coords, z_coords,
                                arcpy.SpatialReference(4759, 115700))

# Print the total rows
print(arcpy.management.GetCount(out_feature_class))