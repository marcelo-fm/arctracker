#-------------------------------------------------------------------------------
# Name: OptimalRegionConnections_Ex_02.py
# Description: Calculates the optimal connections between regions.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputRegionsLayer =
    'https://MyPortal.esri.com/server/rest/services/Hosted/regions/ImageServer'
outputName = 'outOptimalConnections'
inputBarriersLayer =
    'https://MyPortal.esri.com/server/rest/services/Hosted/barriers/ImageServer'
inputCostLayer = 
    'https://MyPortal.esri.com/server/rest/services/Hosted/cost/ImageServer'
outputName02 = 'outNeighborConnections'
distanceMethod = 'GEODESIC'
connectionsWithinRegions = 'GENERATE_CONNECTIONS' 

arcpy.ra.OptimalRegionConnections(inputRegionsLayer, outputName, inputBarriersLayer,
                                  inputCostLayer, outputName02, distanceMethod,connectionsWithinRegions)