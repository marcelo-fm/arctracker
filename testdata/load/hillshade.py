# Name: HillShade_3d_Ex_02.py
# Description: Computes hillshade values for a raster surface.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
outRaster = "C:/output/outhillshd02"
azimuth = 180
altitude = 75
modelShadows = "SHADOWS"
zFactor = 0.348

# Execute HillShade
arcpy.ddd.HillShade(inRaster, outRaster, azimuth, altitude, 
                    modelShadows, zFactor)