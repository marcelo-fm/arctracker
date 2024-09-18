# Name: reclassbytable_example02.py
# Description: Reclassifies the values of the input raster using a remap table.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "slope"
inRemapTable = "remapslope"

# Execute Reclassify
outRaster = ReclassByTable(inRaster, inRemapTable,"FROM","TO","OUT","NODATA")

# Save the output 
outRaster.save("C:/sapyexamples/output/recslope")