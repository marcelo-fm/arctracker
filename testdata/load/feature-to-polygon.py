# Name: FeatureToPolygon_Example2.py
# Description: Use FeatureToPolygon function to construct habitat areas
#              from park boundaries and rivers.

# Import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/parks_analysis.gdb"

# Set local parameters
inFeatures = ["park_boundaries", "rivers"]
outFeatureClass = "c:/output/output.gdb/habitat_areas"
clusTol = "0.05 Meters"

# Use the FeatureToPolygon function to form new areas
arcpy.management.FeatureToPolygon(inFeatures, outFeatureClass, clusTol,
                                  "NO_ATTRIBUTES")