# Description: Delete features from a feature class based on an expression
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/airport.gdb"
 
# Set local variables
inFeatures = "parcels"
outFeatures = "C:/output/output.gdb/new_parcels"
tempLayer = "parcelsLayer"
expression = arcpy.AddFieldDelimiters(tempLayer, "PARCEL_ID") + " = 'Cemetery'"
 

# Run CopyFeatures to make a new copy of the feature class
arcpy.management.CopyFeatures(inFeatures, outFeatures)
 
# Run MakeFeatureLayer
arcpy.management.MakeFeatureLayer(outFeatures, tempLayer)
 
# Run SelectLayerByAttribute to determine which features to delete
arcpy.management.SelectLayerByAttribute(tempLayer, "NEW_SELECTION", 
                                        expression)
 
# Run GetCount and if some features have been selected, 
#  run DeleteFeatures to remove the selected features.
if int(arcpy.management.GetCount(tempLayer)[0]) > 0:
    arcpy.management.DeleteFeatures(tempLayer)