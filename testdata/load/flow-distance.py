#---------------------------------------------------------------------------
# Name: FlowDistance_example02.py
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inStreams = "https://myserver/rest/services/streams/ImageServer"
inSurface = "https://myserver/rest/services/elevation_fill/ImageServer"
outputFlowDistance = "outFlowDistanceVertical2"
inFlowDirection = ""
distanceType = "VERTICAL"

# Execute Flow Distance raster analysis tool
arcpy.ra.FlowDistance(inStreams, inSurface, outputFlowDistance, inFlowDirection, distanceType)