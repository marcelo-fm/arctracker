#-------------------------------------------------------------------------------
# Name: ZonalStatisticsAsTable_Ex_02.py
# Description: Calculates all statistics with defined percentile values  
#              for sea-surface temperature defined by ecological zones.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputZoneRasterOrFeatures = 'https://MyPortal.esri.com/server/rest/services/Hosted/zones/ImageServer'
inputValueRaster = 'https://MyPortal.esri.com/server/rest/services/Hosted/seaSurfaceTemperature/ImageServer'
outputTableName = 'outZSAT'
zoneField = 'temperature'
ignoreNodata = '' 
statisticType = 'PERCENTILE'
percentileValues = [25,75,90]
processAsMultidimensional = 'ALL_SLICES'
percentileInterpolationType = 'NEAREST'

# Execute Multidimensional Zonal Statistics as Table
arcpy.ra.ZonalStatisticsAsTable(inputZoneRasterOrFeatures, inputValueRaster, outputTableName, zoneField,
                                ignoreNodata, statisticType, percentileValues, processAsMultidimensional, 
                                percentileInterpolationType)