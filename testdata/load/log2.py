# Name: Log2_Ex_02.py
# Description: Calculates the base 2 logarithm of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Log2
outLog2 = Log2(inRaster)

# Save the output 
outLog2.save("C:/sapyexamples/output/outlog2")