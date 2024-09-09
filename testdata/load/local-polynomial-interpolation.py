# Name: LocalPolynomialInterpolation_Example_02.py
# Description: Local Polynomial interpolation fits many polynomials, each 
#              within specified overlapping neighborhoods. 
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inPointFeatures = "ca_ozone_pts.shp"
zField = "ozone"
outLayer = "outLPI"
outRaster = "C:/gapyexamples/output/lpiout"
cellSize = 2000.0
power = 2
kernelFunction = "QUARTIC"
bandwidth = ""
useConNumber = ""
conNumber = ""
weightField = ""
outSurface = "PREDICTION"

# Set variables for search neighborhood
majSemiaxis = 300000
minSemiaxis = 300000
angle = 0
smoothFactor = 0.5
searchNeighbourhood = arcpy.SearchNeighborhoodSmooth(majSemiaxis, minSemiaxis,
                                                     angle, smoothFactor)


# Execute LocalPolynomialInterpolation
arcpy.LocalPolynomialInterpolation_ga(inPointFeatures, zField, outLayer, outRaster,
                                      cellSize, power, searchNeighbourhood,
                                      kernelFunction, bandwidth, useConNumber,
                                      conNumber, weightField, outSurface)