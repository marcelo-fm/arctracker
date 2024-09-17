# Name: FeatureEnvelopeToPolygon_Example2.py
# Description: Use FeatureEnvelopeToPolygon function to find 
#              the general extent of features.

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/urban_analysis.gdb"

# Set local variables
inFeatures = "houses"
outFeatureClass = "c:/output/output.gdb/houses_extent"

# Execute FeatureEnvelopeToPolygon
arcpy.FeatureEnvelopeToPolygon_management(inFeatures, outFeatureClass, 
                                          "SINGLEPART")