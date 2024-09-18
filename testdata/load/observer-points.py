# Name: ObserverPoints_Ex_02.py
# Description: Identifies exactly which observer points are visible 
#              from each raster surface location.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inObsPoints = "observers.shp"
zFactor = 1
useEarthCurv = "CURVED_EARTH"
refractionVal = 0.13

# Execute ObserverPoints
outObsPoints = ObserverPoints(inRaster, inObsPoints, zFactor, 
                              useEarthCurv, refractionVal)

# Save the output 
outObsPoints.save("C:/sapyexamples/output/outobspnt02")