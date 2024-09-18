# Name: Negate_Ex_02.py
# Description: Changes the sign (multiplies by -1) of the cell values
#              of the input raster on a pixel-by-pixel basis 
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = "degs"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Negate
outNegate = Negate(inRaster)

# Save the output 
outNegate.save("C:/iapyexamples/output/outnegate")