# Name: Thin_Ex_02.py
# Description: Thins rasterized linear features by 
#              reducing the number of cells 
#              representing the width of the features.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "land"
tolerance = 300

# Execute Thin
thinOut = Thin(inRaster, "NODATA", "FILTER", "SHARP", tolerance)

# Save the output 
thinOut.save("c:/sapyexamples/output/thinoutput")