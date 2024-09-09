# Name: ReclassByASCIIFile_Ex_02.py
# Description: Reclassifies  values of the input raster using an ASCII remap 
#    file.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "slope"
inRemapFile = "remapslope.rmp"
outRaster = "C:/output/recslope"

# Execute Reclassify
arcpt.ReclassByASCIIFile_3d(inRaster, inRemapFile, outRaster)