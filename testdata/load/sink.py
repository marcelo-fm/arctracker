# Name: Sink_Ex_02.py
# Description: Creates a raster identifying all sinks or areas of internal drainage.
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
outSink = Sink(inFlowDirectionRaster)

# Save the output 
outSink.save("C:/sapyexamples/output/outsink02")