# Name: Dissolve_Example2.py
# Description: Dissolve features based on common attributes

# Import system modules
import arcpy

arcpy.env.workspace = "C:/data/Portland.gdb/Taxlots"

# Set local variables
inFeatures = "taxlots"
tempLayer = "taxlotsLyr"
expression = arcpy.AddFieldDelimiters(inFeatures, "LANDUSE") + " <> ''"
outFeatureClass = "C:/output/output.gdb/taxlots_dissolved"
dissolveFields = ["LANDUSE", "TAXCODE"]

# Run MakeFeatureLayer and SelectLayerByAttribute.  This is only to exclude 
# features that are not desired in the output.
arcpy.management.MakeFeatureLayer(inFeatures, tempLayer)
arcpy.management.SelectLayerByAttribute(tempLayer, "NEW_SELECTION", expression)

# Run Dissolve using LANDUSE and TAXCODE as Dissolve Fields
arcpy.management.Dissolve(tempLayer, outFeatureClass, dissolveFields, "", 
                          "SINGLE_PART", "DISSOLVE_LINES")