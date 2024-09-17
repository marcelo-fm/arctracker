# Name: RoundUp_Ex_02.py
# Description: Returns the next higher whole number for each pixel
#              in a raster
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

# Execute RoundUp
outRoundURaster = RoundUp(inRaster)

# Save the output 
outRoundURaster.save("C:/iapyexamples/output/outroundup")