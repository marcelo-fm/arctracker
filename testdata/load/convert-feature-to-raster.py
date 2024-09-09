#-------------------------------------------------------------------------------
# Name: ConvertFeatureToRaster_Ex_02.py
# Description: Convert point features to a raster.
#
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inFeatures = 'https://MyPortal.esri.com/server/rest/services/Hosted/Rainfall/FeatureServer/0'
inField = 'elevation'
outCellSize = '250 Meters'
outRaster = 'outRaster'

# Execute ConvertFeatureToRaster
arcpy.ra.ConvertFeatureToRaster(inFeatures, inField, outRaster, outCellSize)