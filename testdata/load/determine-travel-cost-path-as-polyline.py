#-------------------------------------------------------------------------------
# Name: DetermineTravelCostPathAsPolyline_Ex_02.py
# Description: Calculates the optimum travel cost path.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputSourceLayer =
    'https://MyPortal.esri.com/server/rest/services/Hosted/sources/ImageServer'
inputCostLayer =
    'https://MyPortal.esri.com/server/rest/services/Hosted/costraster/ImageServer'
inputDestinationLayer = 
    'https://MyPortal.esri.com/server/rest/services/Hosted/destinationras/ImageServer'
outputName = 'outTravelPaths'
pathType = 'BEST_SINGLE'

arcpy.ra.DetermineTravelCostPathAsPolyline(inputSourceLayer, inputCostLayer,
                                           inputDestinationLayer, outputName, pathType)