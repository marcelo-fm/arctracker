# Name: GenerateMappingTable.py
# Description: Generate a Mapping Table from the input Data Reference workbook.

# Import system modules
import arcpy

# Set local variables
workbook = "C:/data/DataLoadingWorkspace/DataReference.xlsx"
mapping = "C:/temp/MappingTable.csv"

arcpy.management.GenerateMappingTable(in_workbook=workbook, out_table=mapping)