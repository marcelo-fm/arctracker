# Name: RoundDown_Ex_02.py
# Description: Returns the next lower whole number for each pixel in a raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = "gwhead"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute RoundDown
outRoundDRaster = RoundDown(inRaster)

# Save the output 
outRoundDRaster.save("C:/iapyexamples/output/outrounddown")