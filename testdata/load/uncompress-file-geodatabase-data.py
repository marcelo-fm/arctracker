# Name: UncompressFileGeodatabaseData.py
# Description: Use the UncompressFileGeodatabaseData tool to uncompress a geodatabase

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
geodatabase = "london.gdb"

# Process: Compress the data
arcpy.management.UncompressFileGeodatabaseData(geodatabase)