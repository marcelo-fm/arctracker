# Name: Float_Ex_02.py
# Description: Converts each cell value of a raster into a floating-point representation
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "landuse"

# Execute Float
outFloat = Float(inRaster)

# Save the output 
outFloat.save("C:/sapyexamples/output/outfloat")