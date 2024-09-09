# Name: EBK3D_Example_02.py
# Description: Interpolates 3D points.
# Requirements: Geostatistical Analyst Extension
# Author: Esri

# Import system modules
import arcpy

# Set local variables
in3DPoints = "C:/gapyexamples/input/my3DPoints.shp"
elevationField = "Shape.Z"
valueField = "myValueField"
outGALayer = "myGALayer"
elevationUnit = "METER"
measurementErrorField = "myMEField"
semivariogramModel = "LINEAR"
transformationType = "NONE"
subsetSize = 80
overlapFactor = 1.5
numSimulations = 200
trendRemoval = "FIRST"
elevInflationFactor = 20
radius = 10000
maxNeighbors = 15
minNeighbors = 10
sectorType = "FOUR_SECTORS"
searchNeighborhood = arcpy.SearchNeighborhoodStandard3D(radius, maxNeighbors, minNeighbors, sectorType)
outputElev = 1000
outputType = "PREDICTION"

# Check out the ArcGIS Geostatistical Analyst extension license
arcpy.CheckOutExtension("GeoStats")

# Execute Empirical Bayesian Kriging 3D
arcpy.ga.EmpiricalBayesianKriging3D(in3DPoints, elevationField, valueField, outGALayer, elevationUnit, myMEField,
                                    semivariogramModel, transformationType, subsetSize, overlapFactor, numSimulations,
                                    trendRemoval, elevInflationFactor, searchNeighborhood, outputElev, outputType)