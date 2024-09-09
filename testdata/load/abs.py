# Name: Abs_Ex_02.py
# Description: Calculates the absolute value of cells in a raster 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "negs"

# Execute Abs
outAbs = Abs(inRaster)

# Save the output 
outAbs.save("C:/sapyexamples/output/outabs.tif")