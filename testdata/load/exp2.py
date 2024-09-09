# Name: Exp2_Ex_02.py
# Description: Calculates the base 2 exponential of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute Exp2
outExp2 = Exp2(inRaster)

# Save the output 
outExp2.save("C:/sapyexamples/output/outexp2")