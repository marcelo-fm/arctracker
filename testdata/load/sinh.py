# Name: SinH_Ex_02.py
# Description: Calculates the hyperbolic sine of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute SinH
outSinH = SinH(inRaster)

# Save the output 
outSinH.save("C:/sapyexamples/output/outsinh.tif")