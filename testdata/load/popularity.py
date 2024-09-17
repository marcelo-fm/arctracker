# Name: Popularity_Ex_02.py
# Description: Determines the value in an argument list that is
#              at a certain level of popularity 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPopularityRaster = "cost"
inRaster01 = "degs"
inRaster02 = "negs"
inRaster03 = "fourgrd"

# Execute Popularity
outPopularity = Popularity(inPopularityRaster, [inRaster01, inRaster02, inRaster03])

# Save the output 
outPopularity.save("C:/sapyexamples/output/outpop")