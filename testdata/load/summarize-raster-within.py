#-------------------------------------------------------------------------------
# Name: SummarizeRasterWithin_Ex_02.py
# Description: Calculates the maximum sea-surface temperature at different ecological zones.
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inputZoneLayer = 'https://MyPortal.esri.com/server/rest/services/Hosted/zones/ImageServer'
zoneField = 'temperature'
inputRasterLayertoSummarize = 'https://MyPortal.esri.com/server/rest/services/Hosted/seaSurfaceTemperature/ImageServer'
outputName = 'outSSTRaster'
statisticType = 'MAXIMUM' 
ignoreMissingValues = ''
processAsMultidimensional = 'ALL_SLICES'

# Execute Multidimensional Summarize Raster Within operation
arcpy.ra.SummarizeRasterWithin(inputZoneLayer, zoneField, inputRasterLayertoSummarize,
                               outputName, statisticType, ignoreMissingValues)