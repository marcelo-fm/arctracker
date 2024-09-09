#-------------------------------------------------------------------------------
# Name: CreateSpaceTimeCube.py
# Description: Create a cube representing the counts of Crimes

# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inFeatures = "https://MyGeoAnalyticsMachine.domain.com/geoanalytics/rest/services/DataStoreCatalogs/bigDataFileShares_Crimes/BigDataCatalogServer/Chicago"
outCube = "CrimeCube.nc"

# Execute Create Space Time Cube
arcpy.geoanalytics.CreateSpaceTimeCube(inFeatures, outCube, "1 Kilometers", 
                                       "1 Weeks", "START_TIME")