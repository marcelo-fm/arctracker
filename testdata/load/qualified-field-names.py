# Name: addjoin.py
# Purpose: Join a table to a feature class and have the output unqualified

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
arcpy.env.qualifiedFieldNames = False

# Set local variables    
inFeatures = "Habitat_Analysis.gdb/vegtype"
layerName = "veg_layer"
joinTable = "vegtable.dbf"
joinField = "HOLLAND95"
expression = "vegtable.HABITAT = 1"
outFeature = "Habitat_Analysis.gdb/vegjoin"

# Create a feature layer from the vegtype feature class
arcpy.management.MakeFeatureLayer(inFeatures, layerName)

# Join the feature layer to a table
arcpy.management.AddJoin(layerName, joinField, joinTable, joinField)

# Copy the layer to a new permanent feature class
# Output fields are unqualified, so the field name will 
# not contain the origin table
arcpy.management.CopyFeatures(layerName, outFeature)