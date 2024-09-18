# Name: Log2_Ex_02.py
# Description: Calculates the base 2 logarithm of pixels in a raster
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

# Execute Log2
outLog2 = Log2(inRaster)

# Save the output 
outLog2.save("C:/iapyexamples/output/outlog2")