# Name: BooleanOr_Ex_02.py
# Description: Performs a Boolean Or operation on the cell values of
#              two input rasters
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

# Execute BooleanOr
outBooleanOr = BooleanOr(inRaster1, inRaster2)

# Save the output 
outBooleanOr.save("C:/sapyexamples/output/outboolor")