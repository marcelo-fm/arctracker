# Name: ASinH_Ex_02.py
# Description: Calculates the inverse hyperbolic sine of cells
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

# Execute ASinH
outASinH = ASinH(inRaster)

# Save the output 
outASinH.save("C:/sapyexamples/output/outasinh.img")