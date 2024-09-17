# Name: EnableEditorTracking_Ex02.py
# Description: Enables editor tracking for all datasets in a geodatabase

# Import system modules
import arcpy
import os

# Set the workspace
workspace = arcpy.GetParameterAsText(0)

# Set the workspace environment
arcpy.env.workspace = "d:/test/data.gdb"

# Get all the stand alone tables and feature classes
dataList = arcpy.ListTables() + arcpy.ListFeatureClasses()

# For feature datasets, get all of the feature classes
# from the list and add them to the master list
for dataset in arcpy.ListDatasets("", "Feature"):
    arcpy.env.workspace = os.path.join(workspace,dataset)
    dataList += arcpy.ListFeatureClasses()

# Run the EnableEditorTracking tool for each dataset
for dataset in dataList:
    print(f'Enabling tracking on {dataset}')
    arcpy.management.EnableEditorTracking(dataset, "ET_CREATOR",
        "ET_CREATED", "ET_EDITOR", "ET_EDITED", "ADD_FIELDS", "UTC")
print('Enabling complete')