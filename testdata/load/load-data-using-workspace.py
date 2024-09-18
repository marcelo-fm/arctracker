# Name: LoadDataUsingWorkspace.py
# Description: Load the source-target mapping defined in DataReference.xlsx

# Import system modules
import arcpy

# Set local variables
workbook = "C:/data/DataLoadingWorkspace/DataReference.xlsx"

arcpy.management.LoadDataUsingWorkspace(in_workbook=workbook)