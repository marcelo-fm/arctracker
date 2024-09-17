# Name: SquareRoot_Ex_02.py
# Description: Calculates the square root of the pixels in a raster
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

# Execute SquareRoot
outSQRT = SquareRoot(inRaster)

# Save the output 
outSQRT.save("C:/iapyexamples/output/outsqrt")