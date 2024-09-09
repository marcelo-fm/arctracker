# Name: ContourWithBarriers_3d_Ex_02.py
# Description: Creates contours from a raster surface.  The inclusion of 
#     barrier features will allow one to independently generate contours on
#     either side of a barrier.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
inBarrier = "elevation_barrier.shp"
inTextFile = ""
explicitValues = "NO_EXPLICIT_VALUES_ONLY"
contourInterval = 200
contourList = "600; 935; 1237.4"
baseContour = 0
outContours = "C:/output/outcwb.shp"

# Execute Contour
arcpy.ddd.ContourWithBarriers(inRaster, outContours, inBarrier, "POLYLINES", 
                              inTextFile, explicitValues, baseContour, 
                              contourInterval, "", contourList, "")