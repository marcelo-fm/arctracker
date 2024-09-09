#-------------------------------------------------------------------------------
# Name: Nibble_Ex_02.py
# Description: Replaces cells of a raster corresponding to a mask 
#              with the values of the nearest neighbors within defines zones.
#
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputLayer      = "https://MyPortal.esri.com/server/rest/services/Hosted/inras/ImageServer"
inputMaskLayer  = "https://MyPortal.esri.com/server/rest/services/Hosted/inmask/ImageServer"
outputName      = "outnibbled2"
nibbleValuesOpt = "DATA_ONLY"
nibbleNodataOpt = "PROCESS_NODATA"
inputZoneLayer  = "https://MyPortal.esri.com/server/rest/services/Hosted/inzones/ImageServer"

arcpy.ra.Nibble(inputLayer, inputMaskLayer, outputName, nibbleValuesOpt, 
                nibbleNodataOpt, inputZoneLayer)