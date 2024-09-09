# Name: BitwiseXOr_Ex_02.py
# Description: Performs a Bitwise XOr operation on the binary values
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

# Execute BitwiseXOr
outBitwiseXOr = BitwiseXOr(inRaster1, inRaster2)

# Save the output 
outBitwiseXOr.save("C:/sapyexamples/output/outbitwisexor.img")