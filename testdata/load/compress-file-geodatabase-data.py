# Name: CompressFileGeodatabaseData.py
# Description: Use the CompressFileGeodatabaseData tool to compress a geodatabase

# import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
geodatabase = "london.gdb"
lossless = "Lossless compression"

# Process: Compress the data
arcpy.management.CompressFileGeodatabaseData(geodatabase, lossless)