# Name: Cos_Ex_02.py
# Description: Calculates the cosine of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Cos
outCos = Cos(inRaster)

# Save the output 
outCos.save("C:/sapyexamples/output/outcos.tif")