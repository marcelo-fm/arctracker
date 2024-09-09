#-------------------------------------------------------------------------------
# Name: MergeLayers.py
# Description: Merge two layers containing parcel information.
#
# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inputFeatures = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/parcels_west/FeatureServer/0"
mergeFeatures = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/east_parcels/FeatureServer/0"
mergingAttributes = [["CODE", "MATCH", "ID"], ["globalid", "REMOVE"]]
outFS = "all_parcels"
dataStore = "SPATIOTEMPORAL_DATA_STORE"

# Execute Merge Layers
arcpy.geoanalytics.MergeLayers(inputFeatures, mergeFeatures, outFS, 
                               mergingAttributes, dataStore)