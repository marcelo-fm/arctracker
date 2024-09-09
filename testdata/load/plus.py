# Name: Plus_Ex_02.py
# Description: Adds the values of two rasters on a cell-by-cell basis.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "cost"
inRaster2 = "degs"

# Execute Plus
outPlus = Plus(inRaster1, inRaster2)

# Save the output 
outPlus.save("C:/sapyexamples/output/outplus")