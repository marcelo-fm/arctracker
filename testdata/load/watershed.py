#---------------------------------------------------------------------------
# Name: Watershed_example02.py
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inFlowDirection = "https://myserver/rest/services/flowdir/ImageServer"
inPourPoint = "https://myserver/rest/services/streamlink/ImageServer"
outputWatershed = "outWatershed2"

# Execute Watershed raster analysis tool
arcpy.ra.Watershed(inFlowDirection, inPourPoint, outputWatershed)