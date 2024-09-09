# Name: DeleteIdentical_Example2.py
# Description: Delete identical features in a dataset based on Shape (geometry) and a TEXT field.

# Import system modules
import arcpy

arcpy.env.overwriteOutput = True

# Set workspace environment
arcpy.env.workspace = "C:/data/sbfire.gdb"

# Set input feature class
in_dataset = "fireincidents"

# Set the field on which the identical records are found
fields = ["Shape", "INTENSITY"]

# Set the XY tolerance within which identical records will be deleted
xy_tol = "0.02 Miles"

# Set the Z tolerance to default
z_tol = ""

# Run Delete Identical 
arcpy.management.DeleteIdentical(in_dataset, fields, xy_tol, z_tol)