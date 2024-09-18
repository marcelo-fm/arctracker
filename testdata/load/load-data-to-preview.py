# Name: LoadDataToPreview.py
# Description: Load the source-target mapping defined in DataReference.xlsx to a preview geodatabase

# Import system modules
import arcpy

# Set local variables
workbook = "C:/data/DataLoadingWorkspace/DataReference.xlsx"
folder = "C:/temp"

arcpy.management.LoadDataToPreview(in_workbook=workbook, out_folder=folder)