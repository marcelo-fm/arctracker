# Name: Viewshed_3d_Ex_02.py
# Description: Determines the raster surface locations visible to a set of
#              observer features.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
inObserverFeatures = "observers.shp"
outViewshed = "C:/output/outvwshd02"
zFactor = 2
useEarthCurvature = "CURVED_EARTH"
refractivityCoefficient = 0.15

# Execute Viewshed
arcpy.ddd.Viewshed(inRaster, inObserverFeatures, outViewshed, zFactor,
                   useEarthCurvature, refractivityCoefficient)