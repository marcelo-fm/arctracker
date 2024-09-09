# Name: ExtractByMask_Ex_02.py
# Description: Extracts the cells of a elevation raster for all areas outside of the mask features.
#     Keeping the output extent of the input elevation raster. 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "elevation"
inMaskData = "mask.shp"
extraction_area = "OUTSIDE"
analysis_extent = "elevation"


# Execute ExtractByMask
outExtractByMask = ExtractByMask(inRaster, inMaskData, extraction_area, analysis_extent)

# Save the output 
outExtractByMask.save("C:/sapyexamples/output/extractmask")