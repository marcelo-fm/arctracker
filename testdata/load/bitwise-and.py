# Name: BitwiseAnd_Ex_02.py
# Description: Performs a Bitwise And operation on the binary values
#              of two input rasters
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

# Execute BitwiseAnd
outBitwiseAnd = BitwiseAnd(inRaster1, inRaster2)

# Save the output 
outBitwiseAnd.save("C:/sapyexamples/output/outband")