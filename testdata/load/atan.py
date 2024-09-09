# Name: ATan_Ex_02.py
# Description: Calculates the inverse tangent of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute ATan
outATan = ATan(inRaster)

# Save the output 
outATan.save("C:/sapyexamples/output/outatan.tif")