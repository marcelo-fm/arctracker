# Name: GASetModelParameter_Example_02.py
# Description: Sets parameter value in an existing geostatistical model source.
# Requirements: Geostatistical Analyst Extension

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/gapyexamples/data"

# Set local variables
modelSource = "C:/gapyexamples/data/kriging.lyr"
xmlPath = "/model[@name = 'Kriging']/model[@name = 'Variogram']/value[@name = 'Nugget']"
newValue = 1
outModel = "C:/gapyexamples/output/outModel.xml"

# Execute GASetModelParameter
newParam = arcpy.GASetModelParameter_ga(modelSource, xmlPath, newValue, outModel)

# Show results
print(newParam)