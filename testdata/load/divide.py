# Name: Divide_Ex_02.py
# Description: Divides the values of two rasters on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = "elevation"
inRaster02 = "landuse"

# Execute Divide
outDivide = Divide(inRaster01, inRaster02)

# Save the output 
outDivide.save("C:/sapyexamples/output/outdivide")