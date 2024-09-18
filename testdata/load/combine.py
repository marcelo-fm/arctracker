# Name: Combine_Ex_02.py
# Description: Combines multiple rasters such that a unique value is
#              assigned to each unique combination of input values
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster01 = "filter"
inRaster02 = "zone"
inRaster03 = "source.img"
inRaster04 = "dec.tif"

# Execute Combine
outCombine = Combine([inRaster01,inRaster02,inRaster03,inRaster04])

# Save the output 
outCombine.save("C:/sapyexamples/output/outcombine")