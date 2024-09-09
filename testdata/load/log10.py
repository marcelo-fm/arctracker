# Name: Log10_Ex_02.py
# Description: Calculates the base 10 logarithm of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Log10
outLog10 = Log10(inRaster)

# Save the output 
outLog10.save("C:/sapyexamples/output/outlog10")