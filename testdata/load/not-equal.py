# Name: NotEqual_Ex_02.py
# Description: Performs a relational not-equal operation on two
#              inputs on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "negs"

# Execute NotEqual
outNotEqual = NotEqual(inRaster1, inRaster2)

# Save the output 
outNotEqual.save("C:/sapyexamples/output/outnotequal")