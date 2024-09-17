# Name: Mod_Ex_02.py
# Description: Finds the remainder of the first raster when divided by
#              the second raster on a pixel-by-pixel basis
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

# Execute Mod
outMod = Mod(inRaster1, inRaster2)

# Save the output 
outMod.save("C:/iapyexamples/output/outmod")