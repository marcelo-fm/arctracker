# Name: Pick_Ex_02.py
# Description: Assigns output values using one of a list of rasters
#              determined by the value of an input raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inPositionRas = "inzone_MB"
inRas01 = "Ras1_MB"
inRas02 = "Ras2_MB"
inRas03 = "Ras3_MB"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute Pick
outPick = Pick(inPositionRaster, [inRas01, inRas02, inRas03], "MULTI_BAND")

# Save the output 
outPick.save("C:/sapyexamples/output/outpick")