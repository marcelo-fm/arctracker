# Name: ACosH_Ex_02.py
# Description: Calculates the inverse hyperbolic cosine of cells
#              in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute ACosH
outACosH = ACosH(inRaster)

# Save the output 
outACosH.save("C:/sapyexamples/output/outacosh")