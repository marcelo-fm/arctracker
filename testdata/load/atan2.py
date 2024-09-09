# Name: ATan2_Ex_02.py
# Description: Calculates the inverse tangent of cells based
#              on (y, x) values from two rasters
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "negs"

# Execute ATan2
outATan2 = ATan2(inRaster1, inRaster2)

# Save the output 
outATan2.save("C:/sapyexamples/output/outatan2.tif")