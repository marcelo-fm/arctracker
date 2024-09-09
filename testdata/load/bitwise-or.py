# Name: BitwiseOr_Ex_02.py
# Description: Performs a Bitwise Or operation on the binary values
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

# Execute BitwiseOr
outBitwiseOr = BitwiseOr(inRaster1, inRaster2)

# Save the output 
outBitwiseOr.save("C:/sapyexamples/output/outbitwiseor.tif")