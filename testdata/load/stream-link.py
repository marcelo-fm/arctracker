#---------------------------------------------------------------------------
# Name: StreamLink_example02.py
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inStreams = "https://myserver/rest/services/streams/ImageServer"
inFlowDirection = "https://myserver/rest/services/flowdir/ImageServer"
outputStreamLink = "outStreamLink2"

# Execute Stream Link raster analysis tool
arcpy.ra.StreamLink(inStreams, inFlowDirection, outputStreamLink)