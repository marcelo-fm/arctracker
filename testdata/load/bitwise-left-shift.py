# Name: BitwiseLeftShift_Ex_02.py
# Description: Performs a Bitwise Left Shift operation on the binary
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

# Execute BitwiseLeftShift
outBitwiseLShift = BitwiseLeftShift(inRaster1, inRaster2)

# Save the output 
outBitwiseLShift.save("C:/sapyexamples/output/outlshift")