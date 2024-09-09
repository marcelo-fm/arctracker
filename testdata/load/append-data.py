# Description: Append February 2018 sales records to your ANNUAL_SALES2018 
#              hosted layer.
#              
#	Caution: AppendData updates your ANNUAL_SALES2018 layer with appended 
#          features.

# Requirements: ArcGIS GeoAnalytics Server

# Import system modules
import arcpy

# Set local variables
inputLayer = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/ANNUAL_SALES2018/FeatureServer/0"
appendLayer = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/DataStoreCatalogs/bigDataFileShares_sales2018/BigDataCatalogServer/FEBRUARY_SALES2018"
appendMethod = "FIELD_MAPPING"
fieldMapping = "Pop_ Population;State_ StateName", 
expressionMapping = "Pop_density $feature.Population/$feature.area_km2;Unused_field null"

# Execute Append Data
arcpy.geoanalytics.AppendData(inputLayer, appendLayer, appendMethod, 
                              fieldMapping, expressionMapping)