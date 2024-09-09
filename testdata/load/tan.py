# Name: Tan_Ex_02.py
# Description: Calculates the tangent of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Tan
outTan = Tan(inRaster)

# Save the output 
outTan.save("C:/sapyexamples/output/outtan.tif")