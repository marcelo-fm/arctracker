# Name: Power_Ex_02.py
# Description: Raises the cells in a raster to the power of the values
#              found in another raster
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

# Execute Power
outPower = Power(inRaster1, inRaster2)

# Save the output 
outPower.save("C:/sapyexamples/output/outpower.img")