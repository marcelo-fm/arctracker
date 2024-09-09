#-------------------------------------------------------------------------------
# Name: CopyToDataStore.py
# Description: Copy Abandoned Water Line dataset to the relational data store
#				Results will be displayed in your Portal

# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inFeatures = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/Water_Network/FeatureServer/3"
outFS = "AbandonedWater"
dataStore = "RELATIONAL_DATA_STORE"

# Execute Copy to Data Store
arcpy.geoanalytics.CopyToDataStore(inFeatures, outFS, dataStore)