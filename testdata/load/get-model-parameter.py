# Name: GAGetModelParameter_Example_02.py
# Description: Gets model parameter value from an existing geostatistical
#              model source.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
modelSource = "C:/gapyexamples/data/kriging.lyr"
xmlPath = "/model[@name = 'Kriging']/model[@name = 'Variogram']/value[@name = 'Nugget']"

# Execute GAGetModelParameter
outParam = arcpy.GAGetModelParameter_ga(modelSource, xmlPath)

# Show results
print(outParam)