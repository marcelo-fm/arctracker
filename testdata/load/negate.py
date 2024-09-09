# Name: Negate_Ex_02.py
# Description: Changes the sign (multiplies by -1) of the cell values
#              of the input raster on a cell-by-cell basis 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Negate
outNegate = Negate(inRaster)

# Save the output 
outNegate.save("C:/sapyexamples/output/outnegate")