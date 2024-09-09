# Name: BitwiseNot_Ex_02.py
# Description: Performs a Bitwise Complement operation on the
#              binary value of an input raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute BitwiseNot
outBitwiseNot = BitwiseNot(inRaster)

# Save the output 
outBitwiseNot.save("C:/sapyexamples/output/outbitnot")