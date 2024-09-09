#---------------------------------------------------------------------------
# Name: FlowAccumulation_example02.py
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inFlowDirection = "https://myserver/rest/services/flowdir/ImageServer"
outputFlowAccumulation = "outFlowAccumulation2"
inWeight = ""
dataType = "DOUBLE"

# Execute Flow Accumulation raster analysis tool
arcpy.ra.FlowAccumulation(inFlowDirection, outputFlowAccumulation, inWeight, dataType)