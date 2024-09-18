# Name: Power_Ex_02.py
# Description: Raises the pixels in a raster to the power of the values
#              found in another raster
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster1 = "degs"
inRaster2 = "cost"

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Power
outPower = Power(inRaster1, inRaster2)

# Save the output 
outPower.save("C:/iapyexamples/output/outpower.img")