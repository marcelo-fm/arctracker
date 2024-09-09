# Name: EBKRegressionPrediction_Example_02.py
# Description: Interpolates housing prices using EBK Regression Prediction
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gaexamples/data.gdb"

# Set local variables
inDepFeatures = "HousingSales_Points"
inDepField = "SalePrice"
inExplanRasters = ["AREASQFEET", "NUMBATHROOMS", "NUMBEDROOMS","TOTALROOMS"]
outLayer = "outEBKRP_layer"
outRaster = "outEBKRP_raster"
outDiagFeatures = "outEBKRP_features"
inDepMeField = ""
minCumVariance = 97.5
outSubsetFeatures = ""
depTransform = ""
semiVariogram= "K_BESSEL"
maxLocalPoints = 50
overlapFactor = 1
numberSinulations = 200
radius = 100000
searchNeighbourhood = arcpy.SearchNeighborhoodStandardCircular(radius)

# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute EBKRegressionPrediction
arcpy.EBKRegressionPrediction_ga(inDepFeatures, inDepField, inExplanRasters,
                outLayer, outRaster, outDiagFeatures, inDepMeField, minCumVariance,
                outSubsetFeatures, depTransform, semiVariogram, maxLocalPoints,
                overlapFactor, numberSinulations, searchNeighbourhood)