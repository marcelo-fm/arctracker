# Name: Hillshade_Ex_02.py
# Description: Computes hillshade values for a raster surface.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
azimuth = 180
altitude = 75
modelShadows = "SHADOWS"
zFactor = 0.348

# Execute HillShade
outHillShade = Hillshade(inRaster, azimuth, altitude, modelShadows, zFactor)

# Save the output 
outHillShade.save("C:/sapyexamples/output/outhillshd02")