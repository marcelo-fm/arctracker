# Name: Square_Ex_02.py
# Description: Calculates the square of the pixels in a raster
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

# Execute Square
outSquare = Square(inRaster)

# Save the output 
outSquare.save("C:/iapyexamples/output/outsquare")