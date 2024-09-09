# Name: _Ex_02.py
# Description: 
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inFlowDirectionRaster = "flowdir"
inWeightRaster = ""
directionType = "DOWNSTREAM"

# Execute 
outFlowLength = FlowLength(inFlowDirectionRaster, directionType, inWeightRaster)

# Save the output 
outFlowLength.save("c:/sapyexamples/output/outflowlen02.tif")