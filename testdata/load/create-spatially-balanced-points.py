# Name: CreateSpatiallyBalancedPoints_Example_02.py
# Description: This tool generates a set of sample points based on inclusion
#   probabilities. The resulting sample design is spatially balanced, meaning
#   that the spatial independence between samples is maximized, making the 
#   design more efficient than sampling the study area at random.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inProb = "ca_prob"
numberPoints = 10
outPoints = "C:/gapyexamples/output/csbp"

# Execute CreateSpatiallyBalancedPoints
arcpy.CreateSpatiallyBalancedPoints_ga(inProb, numberPoints, outPoints)