# Name: SplineWithBarriers_3d_Ex_02.py
# Description: Interpolate a series of point features onto a
#    rectangular raster, using optional barriers, using a
#    minimum curvature spline technique.
# Requirements: 3D Analyst Extension.

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
inBarrierFeature = "ca_ozone_barrier.shp"
cellSize = 2000.0
outRaster = "C:/output/splinebout"

# Execute Spline with Barriers
arcpy.ddd.SplineWithBarriers(inPntFeat, zField, inBarrierFeature,
                             cellSize, outRaster)