#-------------------------------------------------------------------------------
# Name: DetermineTravelCostPathstoDestinations_Ex_02.py
# Description: Calculates the optimum travel cost path.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputSourceLayer =
    'https://MyPortal.esri.com/server/rest/services/Hosted/sources/ImageServer'
inputCostLayer =
    'https://MyPortal.esri.com/server/rest/services/Hosted/costraster/ImageServer'
inputBackLinkLayer = 
    'https://MyPortal.esri.com/server/rest/services/Hosted/backlinkras/ImageServer'
outputName = 'outTravelPathsRaster'
destField = 'dest1'
pathType = 'BEST_SINGLE'

arcpy.ra.DetermineTravelCostPathstoDestinations(inputSourceLayer, inputCostLayer,
                                                inputBackLinkLayer, outputName, 
                                                destField, pathType)