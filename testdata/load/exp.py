# Name: Exp_Ex_02.py
# Description: Calculates the base e exponential of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "landuse"

# Execute Exp
outExp = Exp(inRaster)

# Save the output 
outExp.save("C:/sapyexamples/output/outexp")