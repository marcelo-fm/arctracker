# Name: GaussianGeostatisticalSimulations_Example_02.py
# Description: This tool performs conditional or unconditional geostatistical
#              simulation based on a Simple Kriging model.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"
numRealizations = 10
outWorkspace = "C:/gapyexamples/output"
cellSize = 2000
prefix = "ggs"
rasstatType = "MEAN"
conFeatures = ""
conField = ""
boundingData = ""
savesimRasters = ""
quantile = ""
threshold = ""
statsPolygons = ""
errorField = ""

# Execute GaussianGeostatisticalSimulations
arcpy.GaussianGeostatisticalSimulations_ga(
    inLayer, numRealizations, outWorkspace, prefix, conFeatures, conField, 
    cellSize, boundingData, savesimRasters, quantile, threshold, 
    statsPolygons, rasstatType, errorField)