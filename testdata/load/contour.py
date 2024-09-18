# Name: Contour_Ex_02.py
# Description: Creates contours or isolines from a raster surface.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
contourInterval = 200
baseContour = 0
outContours = "C:/sapyexamples/output/outcontours02.shp"

# Execute Contour
Contour(inRaster, outContours, contourInterval, baseContour)