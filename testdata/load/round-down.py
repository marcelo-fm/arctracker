# Name: RoundDown_Ex_02.py
# Description: Returns the next lower whole number for each cell in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "gwhead"

# Execute RoundDown
outRoundDRaster = RoundDown(inRaster)

# Save the output 
outRoundDRaster.save("C:/sapyexamples/output/outrounddown")