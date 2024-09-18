# Description: Delete unnecessary fields from a feature class or table.
 
# Import system modules
import arcpy
 
# Get user-supplied input and output arguments
inTable = arcpy.GetParameterAsText(0)
updatedTable = arcpy.GetParameterAsText(1)

# Describe the input (need to test the dataset and data types)
desc = arcpy.Describe(inTable)

# Make a copy of the input (so you can maintain the original as is)
if desc.datasetType == "FeatureClass":
    arcpy.management.CopyFeatures(inTable, updatedTable)
else:
    arcpy.management.CopyRows(inTable, updatedTable)

# Use ListFields to get a list of field objects
fieldObjList = arcpy.ListFields(updatedTable)

# Create an empty list that will be populated with field names        
fieldNameList = []

# For each field in the object list, add the field name to the
# name list. Exclude required fields to prevent errors
for field in fieldObjList:
    if not field.required:
        fieldNameList.append(field.name)

# dBASE tables require a field other than an OID and Shape. If this is
# the case, retain an extra field (the first one in the original list)
if desc.dataType in ["ShapeFile", "DbaseTable"]:
    fieldNameList = fieldNameList[1:]

# Run DeleteField to delete all fields in the field list. 
arcpy.management.DeleteField(updatedTable, fieldNameList)