# Name: AttributeSelection.py
# Purpose: Join a table to a feature class and select the desired attributes

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/Habitat_Analysis.gdb"
# The qualifiedFieldNames environment is used by Copy Features when persisting 
# the join field names.
arcpy.env.qualifiedFieldNames = False

# Set local variables
inFeatures = "vegtype"
joinTable = "vegtable"
joinField = "HOLLAND95"
expression = "vegtable.HABITAT = 1"
outFeature = "vegjoin"

# Join the feature layer to a table
veg_joined_table = arcpy.management.AddJoin(inFeatures, joinField, joinTable, 
                                            joinField)

# Select desired features from veg_layer
arcpy.management.SelectLayerByAttribute(veg_joined_table, "NEW_SELECTION", 
                                        expression)

# Copy the layer to a new permanent feature class
result = arcpy.management.CopyFeatures(veg_joined_table, outFeature)

# See field names and aliases
resultFields = arcpy.ListFields(result)
print([field.name for field in resultFields])
print([field.aliasName for field in resultFields])