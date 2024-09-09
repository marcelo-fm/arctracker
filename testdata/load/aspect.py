# Name: Aspect_3d_Ex_02.py
# Description: Derives aspect from a raster surface.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outAspect = "C:/output/outaspect2"
method = "GEODESIC"
zUnit = "FOOT"

# Check out the ArcGIS 3D Analyst extension license
arcpy.CheckOutExtension("3D")

# Execute Aspect
arcpy.ddd.Aspect(inRaster, outAspect, method, zUnit)