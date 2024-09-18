# Name: reclassify_example02.py
# Description: Reclassifies the values in a raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "landuse"
reclassField = "LANDUSE"
remap = RemapValue([["Brush/transitional", 0], ["Water", 1],["Barren land", 2]])

# Execute Reclassify
outReclassify = Reclassify(inRaster, reclassField, remap, "NODATA")

# Save the output 
outReclassify.save("C:/sapyexamples/output/outreclass02")