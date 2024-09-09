'''
TabulateArea.py
Description: Shows how to wrap the TabulateIntersection tool to create a TabulateArea script tool
Requirements: Polygon Zone Feature Class, Polygon Class Feature Class

'''
import arcpy
import sys
import os

def AddMsgAndPrint(msg, severity=0):
    # Adds a Message (in case this is run as a tool)
    # and also prints the message to the screen (standard output)
    print(msg)

    # Split the message on \n first, so that if it's multiple lines, 
    # a GPMessage will be added for each line
    try:
        for string in msg.split('\n'):
            # Add appropriate geoprocessing message 
            if severity == 0:
                arcpy.AddMessage(string)
            elif severity == 1:
                arcpy.AddWarning(string)
            elif severity == 2:
                arcpy.AddError(string)
    except:
        pass

## Get Parameters
zoneFC = arcpy.GetParameterAsText(0)
zoneFld = arcpy.GetParameterAsText(1) # Only allow one field
classFC = arcpy.GetParameterAsText(2)
outTab = arcpy.GetParameterAsText(3)
classFld = arcpy.GetParameterAsText(4) # Optional and only allow one field
sum_Fields = ""
xy_tol = ""
outUnits = arcpy.GetParameterAsText(5)

## Validate parameters
# Inputs can only be polygons
zoneDesc = arcpy.Describe(zoneFC)
classDesc = arcpy.Describe(classFC)
if zoneDesc.shapeType != "Polygon" or classDesc.shapeType != "Polygon":
    AddMsgAndPrint("Inputs must be of type polygon.", 2)
    sys.exit()
    
# Only one zone field and class field
if zoneFld != "":
    if zoneFld.find(";") > -1 or classFld.find(";") > -1:
        AddMsgAndPrint("A maximum of one zone and/or class field is allowed.", 2)
        sys.exit()

# Run TabulateIntersection
try:
    arcpy.analysis.TabulateIntersection(zoneFC, zoneFld, classFC, outTab, 
                                        classFld, sum_Fields, xy_tol, outUnits)
except:
    arcpy.AddMessage("Tabulate Intersection Failed.")

AddMsgAndPrint(arcpy.GetMessages(), 0)