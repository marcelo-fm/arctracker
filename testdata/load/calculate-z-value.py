# Name: CalculateZValue_Example_02.py
# Description: Uses the interpolation model in a geostatistical 
#              layer to predict a value at a single location.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
inGALayer = "C:/gapyexamples/data/Kriging.lyr"
pointCoord = "-2000000 -50000"

# Execute CalculateZValue
outCZV = arcpy.GACalculateZValue_ga(inGALayer, pointCoord)

# Print results
print(outCZV)