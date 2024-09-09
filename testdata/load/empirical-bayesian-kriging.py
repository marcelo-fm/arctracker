# Name: EmpiricalBayesianKriging_Example_02.py
# Description: Bayesian kriging approach whereby many models created around the
#   semivariogram model estimated by the restricted maximum likelihood algorithm is used.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outEBK"
outRaster = "C:/gapyexamples/output/ebkout"
cellSize = 10000.0
transformation = "EMPIRICAL"
maxLocalPoints = 50
overlapFactor = 0.5
numberSemivariograms = 100
# Set variables for search neighborhood
radius = 300000
smooth = 0.6
searchNeighbourhood = arcpy.SearchNeighborhoodSmoothCircular(radius, smooth)
outputType = "PREDICTION"
quantileValue = ""
thresholdType = ""
probabilityThreshold = ""
semivariogram = "K_BESSEL"

# Execute EmpiricalBayesianKriging
arcpy.EmpiricalBayesianKriging_ga(inPointFeatures, zField, outLayer, outRaster,
                                  cellSize, transformation, maxLocalPoints, overlapFactor, numberSemivariograms,
                                  searchNeighbourhood, outputType, quantileValue, thresholdType, probabilityThreshold,
                                  semivariogram)