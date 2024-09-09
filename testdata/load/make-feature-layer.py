# Name: makefeaturelayer_example_2.py
# Description:  Uses MakeFeatureLayer with custom field info as input to Intersect

# Import system modules
import arcpy

# Set overwrite option
arcpy.env.overwriteOutput = True

# Set data path
cityboundaries = "C:/data/City.gdb/boundaries"
countyboundaries = "C:/data/City.gdb/counties"

# Get the fields from the input
fields = arcpy.ListFields(cityboundaries)

# Create a fieldinfo object
fieldinfo = arcpy.FieldInfo()

# Iterate through the input fields and add them to fieldinfo
for field in fields:
    if field.name == "POPULATION":
        # Set the Population to have a ratio split policy
        fieldinfo.addField(field.name, field.name, "VISIBLE", "RATIO")
    else:
        fieldinfo.addField(field.name, field.name, "VISIBLE", "NONE")

# Make a layer from the feature class
arcpy.management.MakeFeatureLayer(cityboundaries, "city_boundaries_lyr", fieldinfo)

# Intersect cities and counties, splitting city population proportionally by county
arcpy.analysis.Intersect([["city_boundaries_lyr"],[countyboundaries]], "memory/intersected_city_counties")