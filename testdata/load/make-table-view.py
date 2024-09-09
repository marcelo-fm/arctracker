# Name: MakeTableView_Example2.py
# Description: Uses a FieldInfo object to select a subset of fields and use with MakeTableView

# Import system modules
import arcpy

# Set data path
intable = "C:/data/tables.gdb/crimefreq"

# Get the fields from the input
fields= arcpy.ListFields(intable)

# Create a fieldinfo object
fieldinfo = arcpy.FieldInfo()

# Iterate through the input fields and add them to fieldinfo
for field in fields:
    if field.name == "CRIME_ADDRESS":
        # Make the CRIME_ADDRESS field hidden
        fieldinfo.addField(field.name, field.name, "HIDDEN", "")
    else:
        fieldinfo.addField(field.name, field.name, "VISIBLE", "")

# The created crime_view layer will have fields as set in fieldinfo object
arcpy.management.MakeTableView(intable, "crime_view", "", "", fieldinfo)

# Persist the view to a table
arcpy.management.CopyRows("crime_view", "C:/data/tables.gdb/crime_copy")