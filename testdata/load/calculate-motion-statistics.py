# Name: CalculateMotionStatistics.py
# Description: Calculate speed, acceleration, and bearing for hurricane tracks.
# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inFeatures = "https://mydomain.com/server/rest/services/DataStoreCatalogs/bigDataFileShares_Hurricanes/BigDataCatalogServer/all"
out = "Hurricanes_MotionStats"
trackField = "name"

# Execute Calculate Motion Statistics
arcpy.geoanalytics.CalculateMotionStatistics(inFeatures, out, trackField, 5, 
                                             ["SPEED", "ACCELERATION", "BEARING"], 
                                             "GEODESIC")