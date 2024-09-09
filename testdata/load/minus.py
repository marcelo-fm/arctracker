# Name: Minus_Ex_02.py
# Description: Subtracts the value of the second input raster from the
#              value of the first input raster on a cell-by-cell basis
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

# Execute Minus
outMinus = Minus(inRaster1, inRaster2)

# Save the output 
outMinus.save("C:/sapyexamples/output/outminus.tif")