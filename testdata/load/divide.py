# Name: Divide_Ex_02.py
# Description: Divides the values of two rasters on a pixel-by-pixel basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster01 = "elevation"
inRaster02 = "landuse"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Divide
outDivide = Divide(inRaster01, inRaster02)

# Save the output 
outDivide.save("C:/iapyexamples/output/outdivide")