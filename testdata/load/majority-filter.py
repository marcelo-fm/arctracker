# Name: MajorityFilter_Ex_02.py
# Description: Replaces cells in a raster based on the 
#              majority of their contiguous neighboring cells.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "land"

# Execute MajorityFilter
outMajFilt = MajorityFilter(inRaster, "EIGHT", "HALF")

# Save the output 
outMajFilt.save("c:/sapyexamples/output/majfilter")