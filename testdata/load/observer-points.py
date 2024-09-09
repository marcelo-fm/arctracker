# Name: ObserverPoints_3d_Ex_02.py
# Description: Identifies exactly which observer points are visible 
#              from each raster surface location.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
inObsPoints = "observers.shp"
outRaster = "C:/output/outobspnt02"
zFactor = 1
useEarthCurv = "CURVED_EARTH"
refractionVal = 0.13

# Execute ObserverPoints
arcpy.ddd.ObserverPoints(inRaster, inObsPoints, outRaster, zFactor, 
                         useEarthCurv, refractionVal)