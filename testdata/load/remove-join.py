# AddFieldFromJoin.py
# Description: Add a field to a table, and calculate its values based
#              on the values in a field from a joined table

# Import system modules
import arcpy

# set the environments
arcpy.env.workspace = "C:/data"
arcpy.env.qualifiedFieldNames = "UNQUALIFIED"
    
# Define script parameters    
inFeatures = "Habitat_Analysis.gdb/vegtype"
layerName = "veg_layer"
newField = "description"
joinTable = "vegtable.dbf"
joinField = "HOLLAND95"
calcExpression = "!vegtable.VEG_TYPE!"
outFeature = "Habitat_Analysis.gdb/vegjoin335"
    
# Add the new field
arcpy.management.AddField(inFeatures, newField, "TEXT")
    
# Create a feature layer from the vegtype feature class
arcpy.management.MakeFeatureLayer(inFeatures,  layerName)
    
# Join the feature layer to a table
arcpy.management.AddJoin(layerName, joinField, joinTable, joinField)
    
# Populate the newly created field with values from the joined table
arcpy.management.CalculateField(layerName, newField, calcExpression, "PYTHON")
    
# Remove the join
arcpy.management.RemoveJoin(layerName, "vegtable")
    
# Copy the layer to a new permanent feature class
arcpy.management.CopyFeatures(layerName, outFeature)