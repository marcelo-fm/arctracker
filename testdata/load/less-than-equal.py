# Name: LessThanEqual_Ex_02.py
# Description: Performs a relational less-than-equal operation on two
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

# Execute LessThanEqual
outLTE = LessThanEqual(inRaster1, inRaster2)

# Save the output 
outLTE.save("C:/sapyexamples/output/outlte")