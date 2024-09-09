# Name: AttributeJoin.py
# Purpose: Join a table to a feature class and find one-to-many matches

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data/Habitat_Analysis.gdb"
arcpy.env.qualifiedFieldNames = False

# Set local variables
inFeatures = "vegtype"
joinTable = "vegtable"
joinField = "HOLLAND95"  # Both tables have HOLLAND95 field
outFeatures = "Vegtype_Joined"

# Join the feature layer to a table
val_res = arcpy.management.ValidateJoin(inFeatures, joinField, joinTable, joinField)
matched = int(val_res[0]) 
row_count = int(val_res[1])

print(arcpy.GetMessages())  # Tool messages about the Join

# Validate the join returns matched rows before proceeding
if matched >= 1:
    joined = arcpy.management.AddJoin(inFeatures, joinField, joinTable, joinField)

    # Copy the joined layer to a new permanent feature class
    arcpy.management.CopyFeatures(joined, outFeatures)

print(f"Output Features: {outFeatures} had matches {matched} and created {row_count} records")