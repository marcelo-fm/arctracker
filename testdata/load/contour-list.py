# Name: ContourList_3d_Ex_02.py
# Description: Creates contours or isolines based on a list of contour values.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
contourIntervalList = "600; 935; 1237.4"
outContours = "C:/output/outcontlist.shp"

# Execute ContourList
arcpy.ddd.ContourList(inRaster, outContours, contourIntervalList)