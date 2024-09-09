#---------------------------------------------------------------------------
# Name: FlowDirection_example02.py
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inSurface = "https://myserver/rest/services/elevation_filled/ImageServer"
outputFlowDirection = "outD8FlowDir2"
forceFlow = "NORMAL"
flowDirectionType = "D8"

# Execute Flow Direction raster analysis tool
arcpy.ra.FlowDirection(inSurface, outputFlowDirection, forceFlow, flowDirectionType)