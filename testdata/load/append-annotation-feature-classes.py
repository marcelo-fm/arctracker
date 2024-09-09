# Name: AppendAnnotation_Example.py
# Description: Use AppendAnnotation to append annotation feature classes in a 
#              geodatabase

# import system modules 
import arcpy
import os

# Set environment settings - user specified
# User input geodatabase for annotation location - eg. C:/data/roads.gdb
arcpy.env.workspace = input('Location of geodatabase annotation: ')

# Create list of annotation feature classes within the geodatabase
fcList = arcpy.ListFeatureClasses("", "ANNOTATION")

# Set variables
# User input output feature class name - eg. appendedroadsAnno
outFeatureClass = arcpy.env.workspace + os.sep + \
                  input('Output annotation feature class name: ')
refScale = 1200
createClasses = "CREATE_CLASSES"
symbolReq = "NO_SYMBOL_REQUIRED"
autoCreate = "AUTO_CREATE"
autoUpdate = "AUTO_UPDATE"

# Process: Append the annotation feature classes
print("Appending annotation feature classes...")
arcpy.management.AppendAnnotation(fcList, outFeatureClass, refScale, 
                                  createClasses, symbolReq, autoCreate, 
                                  autoUpdate)

print("Annotation feature classes in {} have been appended into {}".format(
    arcpy.env.workspace, outFeatureClass))