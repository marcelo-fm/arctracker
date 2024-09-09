# Name: Merge.py
# Description: Use Merge to move features from two street
#              feature classes into a single dataset with field mapping

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Street feature classes to be merged
oldStreets = "majorrds.shp"
newStreets = "Habitat_Analysis.gdb/futrds"
addSourceInfo = "ADD_SOURCE_INFO"

# Create FieldMappings object to manage merge output fields
fieldMappings = arcpy.FieldMappings()

# Add all fields from both oldStreets and newStreets
fieldMappings.addTable(oldStreets)
fieldMappings.addTable(newStreets)

# Add input fields "STREET_NAM" & "NM" into new output field
fldMap_streetName = arcpy.FieldMap()
fldMap_streetName.addInputField(oldStreets, "STREET_NAM")
fldMap_streetName.addInputField(newStreets, "NM")

# Set name of new output field "Street_Name"
streetName = fldMap_streetName.outputField
streetName.name = "Street_Name"
fldMap_streetName.outputField = streetName

# Add output field to field mappings object
fieldMappings.addFieldMap(fldMap_streetName)

# Add input fields "CLASS" & "IFC" into new output field
fldMap_streetClass = arcpy.FieldMap()
fldMap_streetClass.addInputField(oldStreets, "CLASS")
fldMap_streetClass.addInputField(newStreets, "IFC")

# Set name of new output field "Street_Class"
streetClass = fldMap_streetClass.outputField
streetClass.name = "Street_Class"
fldMap_streetClass.outputField = streetClass  

# Add output field to field mappings object
fieldMappings.addFieldMap(fldMap_streetClass)  

# Remove all output fields from the field mappings, except fields 
# "Street_Class", "Street_Name", & "Distance"
for field in fieldMappings.fields:
    if field.name not in ["Street_Class", "Street_Name", "Distance"]:
        fieldMappings.removeFieldMap(fieldMappings.findFieldMapIndex(field.name))

# Since both oldStreets and newStreets have field "Distance", no field mapping 
# is required

# Use Merge tool to move features into single dataset
uptodateStreets = "C:/output/Output.gdb/allroads"
arcpy.management.Merge([oldStreets, newStreets], uptodateStreets, fieldMappings, 
                       addSourceInfo)