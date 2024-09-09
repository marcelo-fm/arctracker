# Name: LessThan_Ex_02.py
# Description: Performs a relational less-than operation on two inputs
#              on a cell-by-cell basis within the Analysis window
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

# Execute LessThan
outLessThan = LessThan(inRaster1, inRaster2)

# Save the output 
outLessThan.save("C:/sapyexamples/output/outlt")