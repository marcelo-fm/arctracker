# Name: Curvature_3d_Ex_02.py
# Description: Calculates the curvature of a raster surface, 
#              optionally including profile and plan curvature.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outRaster = "C:/output/outcurv02"
zFactor = 1.094

# Execute Curvature
arcpy.ddd.Curvature(inRaster, outRaster, 1.094)