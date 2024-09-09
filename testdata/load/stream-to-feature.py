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
inStreamRaster = "stream"
inFlowDir = "flowdir"
outStreamFeats = "c:/sapyexamples/output.gdb/outstrm02"


# Execute 
StreamToFeature(inStreamRaster, inFlowDir, outStreamFeats,
                 "NO_SIMPLIFY")