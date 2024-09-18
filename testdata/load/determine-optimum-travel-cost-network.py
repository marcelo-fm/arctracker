#-------------------------------------------------------------------------------
# Name: DetermineOptimumTravelCostNetwork_Ex_02.py
# Description: Calculates the optimum travel cost network.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputSourceLayer = 'https://MyPortal.esri.com/server/rest/services/Hosted/sources/ImageServer'
inputCostLayer = 'https://MyPortal.esri.com/server/rest/services/Hosted/costraster/ImageServer'
outputOptimumNetworkName = 'outNetworkRaster'
outputNeighborName = 'outNeighborRaster'

arcpy.ra.DetermineOptimumTravelCostNetwork(inputSourceLayer, zoneField, inputCostLayer,
                               outputOptimumNetworkName, outputNeighborName)