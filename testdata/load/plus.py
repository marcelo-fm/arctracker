# Name: Plus_Ex_02.py
# Description: Adds the values of two rasters on a pixel-by-pixel basis.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = "cost"
inRaster2 = "degs"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Plus
outPlus = Plus(inRaster1, inRaster2)

# Save the output 
outPlus.save("C:/iapyexamples/output/outplus")