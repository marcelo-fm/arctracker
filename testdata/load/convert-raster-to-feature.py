#-------------------------------------------------------------------------------
# Name: ConvertRasterToFeature_Ex_02.py
# Description: Convert a raster to polygon features.
#
# Requirements: ArcGIS Image Server

# Import system modules
import arcpy

# Set local variables
inRaster = 'https://MyPortal.esri.com/server/rest/services/Hosted/Landuse/ImageServer'
inField = 'Value'
outType = 'POLYGON'
simplify = 'SIMPLIFY'
outFeatures = 'outFeatures'
arcpy.ra.ConvertRasterToFeature(inRaster, inField, outType, simplify, outFeatures)