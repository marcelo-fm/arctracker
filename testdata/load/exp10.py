# Name: Exp10_Ex_02.py
# Description: Calculates the base 10 exponential of pixels in a raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = "cost"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Exp10
outExp10 = Exp10(inRaster)

# Save the output 
outExp10.save("C:/iapyexamples/output/outexp10.img")