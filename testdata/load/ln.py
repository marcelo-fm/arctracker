# Name: Ln_Ex_02.py
# Description: Calculates natural logarithm (base e) of pixels in a raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = "elevation"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Ln
outLn = Ln(inRaster)

# Save the output 
outLn.save("C:/iapyexamples/output/outln")