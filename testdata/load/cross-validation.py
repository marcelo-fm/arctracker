# Name: CrossValidation_Example_02.py
# Description: Perform cross validation on an input geostatistical layer.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inLayer = "C:/gapyexamples/data/kriging.lyr"

# Execute CrossValidation
cvResult = arcpy.CrossValidation_ga(inLayer)
print("Root Mean Square error = " + str(cvResult.rootMeanSquare))