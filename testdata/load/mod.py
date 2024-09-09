# Name: Mod_Ex_02.py
# Description: Finds the remainder of the first raster when divided by
#              the second raster on a cell-by-cell basis
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "negs"

# Execute Mod
outMod = Mod(inRaster1, inRaster2)

# Save the output 
outMod.save("C:/sapyexamples/output/outmod")