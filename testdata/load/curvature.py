# Name: Curvature_Ex_02.py
# Description: Calculates the curvature of a raster surface, 
#              optionally including profile and plan curvature.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
zFactor = 1.094

# Execute Curvature
outCurve = Curvature(inRaster, 1.094)

# Save the output 
outCurve.save("C:/sapyexamples/output/outcurv02")