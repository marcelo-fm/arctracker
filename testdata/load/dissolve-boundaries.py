# Name: Dissolve_County_Boundaries.py
# Description: Dissolve county features based on common state name attributes
 
# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/Boundaries.gdb"

# Set local variables
inputLayer = "https://sampleserver6.arcgisonline.com/arcgis/rest/services/USA_counties/FeatureServer/0"
outputName = "USA_State_Boundaries"
statistics = [["population", "SUM"]]
  
# Run DissolveBoundaries using "STATE" as the Dissolve Field
arcpy.gapro.DissolveBoundaries(inputLayer, outputName, "SINGLE_PART",
                               "DISSOLVE_FIELDS", "STATE", statistics)