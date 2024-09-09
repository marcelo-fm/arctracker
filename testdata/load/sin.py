# Name: Sin_Ex_02.py
# Description: Calculates the sine of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Sin
outSin = Sin(inRaster)

# Save the output 
outSin.save("C:/sapyexamples/output/outsin.img")