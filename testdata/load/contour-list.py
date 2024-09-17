# Name: ContourList_Ex_02.py
# Description: CCreates contours or isolines based on a list of contour values.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
contourIntervalList = [600, 935, 1237.4]
outContours = "C:/sapyexamples/output/outcontourlist02.shp"

# Execute ContourList
ContourList(inRaster, outContours, contourIntervalList)