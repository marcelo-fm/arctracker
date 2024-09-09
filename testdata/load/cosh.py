# Name: CosH_Ex_02.py
# Description: Calculates the hyperbolic cosine of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute CosH
outCosH = CosH(inRaster)

# Save the output 
outCosH.save("C:/sapyexamples/output/outcosh.img")