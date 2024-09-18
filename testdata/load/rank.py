# Name: Rank_Ex_02.py
# Description: Returns the value of a set of rasters based on
#              a rank level specified by another raster 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRankRaster = "cost"
inRaster01 = "degs"
inRaster02 = "negs"
inRaster03 = "fourgrd"

# Execute Rank
outRank = Rank(inRankRaster, [inRaster01, inRaster02, inRaster03])

# Save the output 
outRank.save("C:/sapyexamples/output/outrank")