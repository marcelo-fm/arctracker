# Name: Fill_Ex_02.py
# Description: Fills sinks in a surface raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inSurfaceRaster = "elevation"
zLimit = 3.28

# Execute FlowDirection
outFill = Fill(inSurfaceRaster, zLimit)

# Save the output 
outFill.save("C:/sapyexamples/output/outfill02")