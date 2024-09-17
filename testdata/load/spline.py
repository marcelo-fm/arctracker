# Name: Spline_Ex_02.py
# Description: Interpolate a series of point features onto a 
#    rectangular raster using a minimum curvature spline technique.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPntFeat = "ozone_pts.shp"
zField = "ozone"
cellSize = 2000.0
splineType = "REGULARIZED"
weight = 0.1

# Execute Spline
outSpline = Spline(inPntFeat, zField, cellSize, splineType, weight)

# Save the output 
outSpline.save("C:/sapyexamples/output/splineout02")