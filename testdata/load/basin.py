# Name: Basin_Ex_02.py
# Description: Creates a raster delineating all drainage basins.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFlowDirectionRaster = "flowdir"

# Execute FlowDirection
outBasin = Basin(inFlowDirectionRaster)

# Save the output 
outBasin.save("C:/sapyexamples/output/outbasin02")