# Name: ATanH_Ex_02.py
# Description: Calculates the inverse hyperbolic tangent of cells 
#    in a raster
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute TanH
outATanH = ATanH(inRaster)

# Save the output 
outATanH.save("C:/sapyexamples/output/outatanh.img")