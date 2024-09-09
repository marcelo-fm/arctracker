# Name: Viewshed_3d_Ex_02.py
# Description: Determines the raster surface locations visible 
#              to a set of observer features.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "c:/data"

# set local variables
inRaster = "elevation"
inObserverFeatures = "observers.shp"
outRaster = "c:/output/visiout1"
aglOutput = "c:/output/aglout1"
analysisType = "OBSERVERS"
nonVisibleValue = "ZERO"
zFactor = 1
useEarthCurvature = "CURVED_EARTH"
refractivityCoefficient = 0.13
surfaceOffset = 500
observerElevation = 2000
observerOffset = 500
innerRadius = 20000
outerRadius = 100000
horizStartAngle = 45
horizEndAngle = 215
vertUpperAngle = 5
vertLowerAngle = -5

# Execute Visibility
arcpy.ddd.Visibility(inRaster, inObserverFeatures, outRaster, algOutput,
                     analysisType, nonVisibleValue, zFactor, useEarthCurvature,
                     refractivityCoefficient, surfaceOffset, observerElevation,
                     observerOffset, innerRadius, outerRadius, horizStartAngle,
                     horizEndAngle, vertUpperAngle, vertLowerAngle)