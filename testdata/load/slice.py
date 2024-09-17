# Name: Slice_Ex_04.py
# Description: Slices the input raster into 10 zones(classes) based on equal area.
#              Assign NoData cells to have a value of -99 in the output.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
numberZones = 10
baseOutputZone = 5
nodataToValue = -99
classIntervalSize = "" # or None

# Execute Slice
outSlice = Slice(inRaster, numberZones, "EQUAL_AREA", baseOutputZone, nodataToValue, classIntervalSize)

# Save the output
outSlice.save("C:/sapyexamples/output/elev_slice_04.tif")