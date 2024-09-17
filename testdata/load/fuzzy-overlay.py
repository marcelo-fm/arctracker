# Name: FuzzyOverlay_Ex_02.py
# Description: Combine fuzzy membership rasters data together based on 
#    selected overlay type ("GAMMA" in this case). 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRasterList = ["fzymembout1", "fzymembout2"]

# Execute FuzzyMembership
outFzyOverlay = FuzzyOverlay(inRasterList, "GAMMA", 0.9)

# Save the output
outFzyOverlay.save("c:/sapexamples/output/fuzzoverlay")