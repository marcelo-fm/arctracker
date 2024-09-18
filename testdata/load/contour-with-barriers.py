# Name: ContourWithBarriers_Ex_02.py
# Description: Creates contours from a raster surface.
#           The inclusion of barrier features will allow one to independently generate contours on either side of a barrier.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inBarrier = "elevation_barrier.shp"
inTextFile = ""
explicitValues = "NO_EXPLICIT_VALUES_ONLY"
contourInterval = 200
contourList = [600, 935, 1237.4]
baseContour = 0
outContours = "C:/sapyexamples/output/outcontourwithbarriers02.shp"

# Execute Contour
ContourWithBarriers(inRaster, outContours, inBarrier, "POLYLINES", inTextFile, 
                    explicitValues, baseContour, contourInterval, "", 
                    contourList, "")