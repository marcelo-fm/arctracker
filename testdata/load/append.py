# Name: Append.py
# Description: Use the Append tool to combine several polygon feature classes

# Import system modules 
import arcpy
import os

# Set environment settings
arcpy.env.workspace = "C:/data/towns.gdb"

# Set local variables
outLocation = "C:/data/output.gdb"
outName = "MA_towns.shp"
schemaType = "NO_TEST"
fieldMappings = ""
subtype = ""

# Process: Append to an existing "amherst" polygon feature class
target = os.path.join(outLocation, "amherst")

# All polygon FCs in the workspace are MA town FCs, you want to append these
# to the target FC. The list will resemble ["amherst", "hadley", "pelham",
# "coldspring"]

fcList = arcpy.ListFeatureClasses("", "POLYGON")

# Create FieldMappings object to manage merge output fields
fieldMappings = arcpy.FieldMappings()

# Add the target table to the field mappings class to set the schema
fieldMappings.addTable(target)

# Add input fields for the town name to TOWNNAME field that matches the 
# target dataset since each input dataset has a different field name for 
# this info
fldMap = arcpy.FieldMap()
fldMap.addInputField("amherst","TOWNNAME")
fldMap.addInputField("hadley","NAME")
fldMap.addInputField("pelham","TOWN_NAME")
fldMap.addInputField("coldspring","TOWN")

# Set name of new output field "TOWNNAME"
townName = fldMap.outputField
townName.name, townName.aliasName, townName.type = "TOWNNAME", "TOWNNAME", "TEXT"
fldMap.outputField = townName

# Add output field to field mappings object
fieldMappings.addFieldMap(fldMap)

# Do the same for the POPULATION field
fldMap = arcpy.FieldMap()
fldMap.addInputField("amherst","POPULATION")
fldMap.addInputField("hadley","POP")
fldMap.addInputField("pelham","POP_2010")
fldMap.addInputField("coldspring","POP")

# Set name of new output field "POPULATION"
pop = fldMap.outputField
pop.name, pop.aliasName, pop.type = "POPULATION", "POPULATION", "LONG"
fldMap.outputField = pop

# Add output field to field mappings object
fieldMappings.addFieldMap(fldMap)

# Process: Append the feature classes to the target feature class
arcpy.management.Append(fcList, os.path.join(outLocation, "amherst"), schemaType, 
                        fieldMappings, subtype)