# Name: Expand_Ex_02.py
# Description: Expands specified zones of a raster 
#              by a specified number of cells.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "filter"
numberCells = 2
zoneValues = [0, 6, -3]

# Execute Expand
outExpand = Expand(inRaster, numberCells, zoneValues)

# Save the output 
outExpand.save("C:/sapyexamples/output/outexpand")