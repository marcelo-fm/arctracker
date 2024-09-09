# Name: RoundUp_Ex_02.py
# Description: Returns the next higher whole number for each cell
#              in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "gwhead"

# Execute RoundUp
outRoundURaster = RoundUp(inRaster)

# Save the output 
outRoundURaster.save("C:/sapyexamples/output/outroundup")