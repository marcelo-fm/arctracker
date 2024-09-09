# Name: Slice_3d_Ex_04.py
# Description: Slices the input raster into 10 zones(classes) based on equal area.
#              Assign NoData cells to have a value of -99 in the output.
# Requirements: 3D Analyst Extension

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"

# Set local variables
inRaster = "elevation"
outRaster = "C:/output/elev_slice_04.tif"
numberZones = 10
baseOutputZone = 5
nodataToValue = -99
classIntervalSize = "" # or None

# Execute Slice
arcpy.ddd.Slice(inRaster, outRaster, numberZones, "EQUAL_AREA", baseOutputZone, nodataToValue, classIntervalSize)