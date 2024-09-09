# Name: StreamOrder_Ex_02.py
# Description: Assigns a numeric order to segments of a raster 
#              representing branches of a linear network.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Set local variables
inStreamRast = "stream"
inFlowDirectionRaster = "flowdir"
orderMethod = "STRAHLER"

# Execute StreamOrder
outStreamOrder = StreamOrder(inStreamRast, inFlowDirectionRaster, orderMethod)

# Save the output 
outStreamOrder.save("c:/sapyexamples/output/outstrmordr02")