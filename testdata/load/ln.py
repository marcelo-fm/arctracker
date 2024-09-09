# Name: Ln_Ex_02.py
# Description: Calculates natural logarithm (base e) of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Execute Ln
outLn = Ln(inRaster)

# Save the output 
outLn.save("C:/sapyexamples/output/outln")