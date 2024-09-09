# Name: ExtractByCircle_Ex_02.py
# Description: Extracts the cells of a raster based on a circle.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = ("elevation")
centerPoint = arcpy.Point(482838.823, 222128.982)
circRadius = 1000
extractType = "INSIDE"

# Execute ExtractByCircle
outExtCircle = ExtractByCircle(inRaster, centerPoint, circRadius, 
                               extractType)

# Save the output 
outExtCircle.save("c:/sapyexamples/output/extcircle02")