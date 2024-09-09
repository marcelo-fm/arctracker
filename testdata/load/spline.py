# Name: Spline_3d_Ex_02.py
# Description: Interpolate a series of points onto a rectangular
#              raster using a minimum curvature spline technique.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outRaster = "C:/output/splineout"
cellSize = 2000.0
splineType = "REGULARIZED"
weight = 0.1

# Execute Spline
arcpy.ddd.Spline(inPointFeatures, zField, outRaster, cellSize, 
                splineType, weight)