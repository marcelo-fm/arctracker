# Name: Exp10_Ex_02.py
# Description: Calculates the base 10 exponential of cells in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "cost"

# Execute Exp10
outExp10 = Exp10(inRaster)

# Save the output 
outExp10.save("C:/sapyexamples/output/outexp10.img")