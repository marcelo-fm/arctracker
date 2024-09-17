# Name: LowestPosition_Ex_02.py
# Description: Determines the position of a raster with the minimum
#              value in a set of rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = "degs"
inRaster02 = "negs"
inRaster03 = "fourgrd"

# Execute LowestPosition
outLowestPosition = LowestPosition([inRaster01, inRaster02, inRaster03])

# Save the output 
outLowestPosition.save("C:/sapyexamples/output/outlp")