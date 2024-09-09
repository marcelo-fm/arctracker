# Name: CombinatorialOr_Ex_02.py
# Description: Performs a Combinatorial Or operation on the cell
#              values of two input rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "cost"

# Execute CombinatorialOr
outCOr = CombinatorialOr(inRaster1, inRaster2)

# Save the output 
outCOr.save("C:/sapyexamples/output/outcor")