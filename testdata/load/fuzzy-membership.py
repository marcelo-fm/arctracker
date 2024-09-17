# Name: FuzzyMembership_Ex_02.py
# Description: Scales input raster data into values ranging from zero to one
#     indicating the strength of a membership in a set. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"

# Create the FuzzyGaussian algorithm object
midpoint = 1000
spread = 0.4
myFuzzyAlgorithm = FuzzyGaussian(midpoint, spread)

# Execute FuzzyMembership
outFuzzyMember = FuzzyMembership(inRaster, myFuzzyAlgorithm)

# Save the output
outFuzzyMember.save("c:/sapyexamples/fzymemb2")