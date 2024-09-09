# Name: IsNull_Ex_02.py
# Description: Find which cell values of the input raster are NoData
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inRaster = "degs"

# Execute IsNull
outIsNull = IsNull(inRaster)

# Save the output 
outIsNull.save("C:/sapyexamples/output/outisnull")