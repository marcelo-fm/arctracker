# Name: GenerateMultidimensionalAnomaly_Ex_02.py
# Description: Generates an anomaly multidimensional raster for
#           ocean temperature data, comparing pixel values with the yearly mean
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "C:/sapyexamples/data"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

""""
Usage: out_multidimensional_raster = GenerateMultidimensionalAnomaly(in_multidimensional_raster,
                                     {variables}, {method}, {temporal_interval})
"""

# Define input parameters
inputFile = "C:/sapyexamples/data/climateData.crf"
variable = "oceantemp"
averageMethod = "PERCENT_DIFFERENCE_FROM_MEAN"
averageInterval = "YEARLY"
ignoreNoData = "DATA"

# Execute GenerateMultidimensionalAnomaly
outYearlyAnomaly = GenerateMultidimensionalAnomaly(inputFile, variable, 
	averageMethod, averageInterval, ignoreNoData)

# Save the output
outYearlyAnomaly.save("C:/sapyexamples/output/TempAnomaly.crf")