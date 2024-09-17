# Name: CreateTable_Example2.py
# Description: Create a table to store temperature data in gnatcatcher habitat areas

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
out_path = "C:/output"
out_name = "habitatTemperatures.dbf"
template = "vegtable.dbf"
config_keyword = ""

# Run CreateTable
arcpy.management.CreateTable(out_path, out_name, template, config_keyword)