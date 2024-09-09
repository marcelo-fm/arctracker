# Name: Contour_3d_Ex_02.py
# Description: Creates contours or isolines from a raster surface.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
contourInterval = 200
baseContour = 0
outContours = "C:/sapyexamples/output/outcontours02.shp"

# Execute Contour
arcpy.ddd.Contour(inRaster, outContours, contourInterval, baseContour)