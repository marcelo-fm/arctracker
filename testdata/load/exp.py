# Name: Exp_Ex_02.py
# Description: Calculates the base e exponential of pixels in a raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = "landuse"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Exp
outExp = Exp(inRaster)

# Save the output 
outExp.save("C:/iapyexamples/output/outexp")