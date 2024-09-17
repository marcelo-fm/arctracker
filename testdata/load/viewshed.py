# Name: Viewshed_Ex_02.py
# Description: Determines the raster surface locations visible to a set of
#              observer features.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inObserverFeatures = "observers.shp"
zFactor = 2
useEarthCurvature = "CURVED_EARTH"
refractivityCoefficient = 0.15

# Execute Viewshed
outViewshed = Viewshed(inRaster, inObserverFeatures, zFactor, 
                       useEarthCurvature, refractivityCoefficient)

# Save the output 
outViewshed.save("C:/sapyexamples/output/outvwshd02")