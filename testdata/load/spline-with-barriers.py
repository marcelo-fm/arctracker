# Name: SplineWithBarriers_Ex_02.py
# Description: Interpolate a series of point features onto a
#    rectangular raster, using optional barriers, using a
#    minimum curvature spline technique.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
inBarrierFeature = "ca_ozone_barrier.shp"
cellSize = 2000.0

# Execute Spline with Barriers
outSplineBarriers = SplineWithBarriers(inPointFeatures,
                          zField, inBarrierFeature, cellSize)

# Save the output
outSplineBarriers.save("C:/sapyexamples/output/splinebout02")