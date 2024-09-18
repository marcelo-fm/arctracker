# Name: reclassbyasciifile_example02.py
# Description: Reclassifies  values of the input raster using an ASCII remap file
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "slope"
inRemapFile = "remapslope.rmp"

# Execute Reclassify
outRaster = ReclassByASCIIFile(inRaster, inRemapFile)

# Save the output 
outRaster.save("C:/sapyexamples/output/recslope")