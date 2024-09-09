# Name: GroupByProximity.py
# Description: Group roads together that touch
#
# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inFeatures = "https://myGeoAnalyticsMachine.domain.com/geoanalytics/rest/services/DataStoreCatalogs/bigDataFileShares_cityData/BigDataCatalogServer/roads"
outFS = "groupedRoads"
overlayType = "TOUCHES"
dataStore = "SPATIOTEMPORAL_DATA_STORE"

# Run Group By Proximity
result = arcpy.geoanalytics.GroupByProximity(inFeatures, outFS, 
                                 overlayType, data_store=dataStore)