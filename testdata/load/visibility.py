# Name: Visibility_Ex_02.py
# Description: Determines the raster surface locations visible to a set of
#                     observer features.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "c:/sapyexamples/data"

# set local variables
inRaster = "elevation"
inObserverFeatures = "observers.shp"
aglOutput = "c:/sapyexamples/output/aglout1"
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
outvis = arcpy.sa.Visibility(inRaster, inObserverFeatures, algOutput, analysisType,
                            nonVisibleValue, zFactor, useEarthCurvature,
                            refractivityCoefficient, surfaceOffset, observerElevation,
                            observerOffset, innerRadius, outerRadius, horizStartAngle,
                            horizEndAngle, vertUpperAngle, vertLowerAngle)

# Save the output
outvis.save("c:/sapyexamples/output/visiout1")