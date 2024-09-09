# Name: ACos_Ex_02.py
# Description: Calculates the inverse cosine of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute ACos
outACos = ACos(inRaster)

# Save the output 
outACos.save("C:/sapyexamples/output/outacos")