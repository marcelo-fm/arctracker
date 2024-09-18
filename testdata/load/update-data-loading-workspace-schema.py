# Name: UpdateDataLoadingWorkspace.py
# Description: Create a copy of a Data Loading Workspace and update all mapping
#              and domain workbooks.

# Import system modules
import arcpy

# Set local variables
workbook = "C:/data/DataLoadingWorkspace/DataReference.xlsx"

arcpy.management.UpdateDataLoadingWorkspace(in_workbook=workbook)