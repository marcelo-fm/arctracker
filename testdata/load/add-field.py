# Name: AddField_Example2.py
# Description: Add a pair of new fields to a table
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data/airport.gdb"
 
# Set local variables
inFeatures = "schools"
fieldName1 = "ref_ID"
fieldPrecision = 9
fieldAlias = "refcode"
fieldName2 = "status"
fieldLength = 10

# Run AddField twice for two new fields
arcpy.management.AddField(inFeatures, fieldName1, "LONG", fieldPrecision,
                          field_alias=fieldAlias, field_is_nullable="NULLABLE")

arcpy.management.AddField(inFeatures, fieldName2, "TEXT", 
                          field_length=fieldLength)