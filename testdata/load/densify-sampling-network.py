# Name: DensifySamplingNetwork_Example_02.py
# Description: Densify a sampling network based on a predefined geostatistical
#              kriging layer. It uses, inter alia, the Standard Error of 
#              Prediction map to determine where new locations are required.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/Kriging.lyr"
numberPoints = 2
outPoints = "C:/gapyexamples/output/outDSN"

# Execute DensifySamplingNetworks
arcpy.DensifySamplingNetwork_ga(inLayer, numberPoints, outPoints)