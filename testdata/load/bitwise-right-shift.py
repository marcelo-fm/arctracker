# Name: BitwiseRightShift_Ex_02.py
# Description: Performs a Bitwise Right Shift operation on the binary
#              values of two input rasters
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

# Execute BitwiseRightShift
outBitwiseRShift = BitwiseRightShift(inRaster1, inRaster2)

# Save the output 
outBitwiseRShift.save("C:/sapyexamples/output/outbitrshift.img")