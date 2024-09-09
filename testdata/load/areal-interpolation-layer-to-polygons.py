# Name: ArealInterpolationLayerToPolygons_Example_02.py
# Description: Averages (in the case of Gaussian data) or aggregates (in the cases of Binomial or Poisson)
#    the predictions of an Areal Interpolation layer to a new set of polygons.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inArealInterpolationLayer = "C:/gapyexamples/data/AI_layer.lyr"
inPolygonFeatures = "C:/gapyexamples/data/new_polys.shp"
outFeatureClass = "C:/gapyexamples/output/aiout.shp"
appendAllFields = "FID_ONLY"

# Execute ArealInterpolationLayerToPolygons
arcpy.ArealInterpolationLayerToPolygons_ga(inArealInterpolationLayer, inPolygonFeatures, outFeatureClass, appendAllFields)