# Name: Minus_Ex_02.py
# Description: Subtracts the value of the second input raster from the
#              value of the first input raster on a pixel-by-pixel basis
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "negs"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Minus
outMinus = Minus(inRaster1, inRaster2)

# Save the output 
outMinus.save("C:/iapyexamples/output/outminus.tif")