# Name: BooleanNot_Ex_02.py
# Description: Performs a Boolean complement (NOT) operation on the
#              cell values of an input raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute BooleanNot
outBooleanNot = BooleanNot(inRaster)

# Save the output 
outBooleanNot.save("C:/sapyexamples/output/outboolnot")