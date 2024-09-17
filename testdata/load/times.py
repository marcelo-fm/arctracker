# Name: Times_Ex_02.py
# Description: Multiplies the values of two rasters on a pixel-by-pixel basis.
# Requirements: Image Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.ia import *

# Set environment settings
env.workspace = "C:/iapyexamples/data"

# Set local variables
inRaster = "elevation"
inConstant = 0.3048

# Check out the ArcGIS Image Analyst extension license
arcpy.CheckOutExtension("ImageAnalyst")

# Execute Times
outTimes = Times(inRaster, inConstant)

# Save the output 
outTimes.save("C:/iapyexamples/output/timesout")