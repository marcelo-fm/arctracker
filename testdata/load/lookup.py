# Name: Lookup_3d_Ex_02.py
# Description: Creates a new raster by looking up values found in another 
#     field in the table of the input raster.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "mycity"
lookupField = "land_code"
outRaster = "C:/output/mylandcode"

# Execute Lookup
arcpy.ddd.Lookup(inRaster, lookupField, outRaster)