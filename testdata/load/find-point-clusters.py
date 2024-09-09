#-------------------------------------------------------------------------------
# Name: FindPointClusters.py
# Description: Finds Point Clusters of rodent infestations
#
# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inputPoints = "https://myGeoAnalyticsMachine.domain.com/geoanalytics/rest/services/DataStoreCatalogs/bigDataFileShares_countyData/BigDataCatalogServer/rat_sightings"
minimumPoints = 10
outputName = "RodentClusters"
searchDistance = "1 Kilometers"
dataStore = "SPATIOTEMPORAL_DATA_STORE"
clusterMethod = "DBSCAN"

# Execute Find Point Clusters
arcpy.geoanalytics.FindPointClusters(inputPoints, outputName, mimimumPoints, 
                                     searchDistance, dataStore, clusterMethod)