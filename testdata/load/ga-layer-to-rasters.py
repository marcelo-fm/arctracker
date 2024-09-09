# Name: GALayerToRaster_Example_02.py
# Description: Exports a geostatistical layer to a
#              - prediction raster
#              - standard error of prediction raster
#              - quantile raster
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/output"

# Set local variables
inLayer = "C:/gapyexamples/data/ebk.lyr"
outPredict = "ras_predict"
cellSize = 5000
cellptsHor = 1
cellptsVer = 1

# Execute GALayerToRasters
arcpy.GALayerToRasters_ga(inLayer, outPredict, "PREDICTION", None, cellSize,
                       cellptsHor, cellptsVer,
                       "ras_se PREDICTION_STANDARD_ERROR #;ras_quantile QUANTILE 0.67")