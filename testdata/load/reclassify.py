# Name: Reclassify_3d_Ex_02.py
# Description: Reclassifies the values in a raster.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "landuse"
field = "VALUE"
remapString = "1 9;2 8;3 1;4 6;5 3;6 2;7 1"
outRaster = "C:/output/reclass3d"

# Execute Reclassify
arcpy.ddd.Reclassify(inRaster, field, remapString, outRaster, "DATA")