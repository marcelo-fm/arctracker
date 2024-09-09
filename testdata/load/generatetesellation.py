# Name: GenerateDynamicTessellation.py
# Purpose: Generate a grid of squares over the envelope of a provided feature 
# class.

# Import modules
import arcpy 

# Set paths of features
my_feature = r"C:\data\project.gdb\myfeature"
output_feature = r"C:\data\project.gdb\sqtessellation"

# Describe the input feature and extract the extent
description = arcpy.Describe(my_feature)
extent = description.extent

# Find the width, height, and linear unit used by the input feature class' extent
# Divide the width and height value by three.
# Multiply the divided values together and specify an area unit from the linear 
# unit.
# Should result in a 4x4 grid covering the extent. (Not 3x3 since the squares 
# hang over the extent.)
w = extent.width
h = extent.height
u = extent.spatialReference.linearUnitName
area = "{size} Square{unit}s".format(size=w/3 * h/3, unit=u)

# Use the extent's spatial reference to project the output
spatial_ref = extent.spatialReference

arcpy.management.GenerateTessellation(output_feature, extent, "SQUARE", area, 
                                      spatial_ref)