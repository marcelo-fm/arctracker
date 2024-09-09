# Name: Analyze_Example.py
# Description: Gathers statistics for the indexes on the business table of the input dataset

# Import system modules
import arcpy

# Set local variables
inDataset = "c:/Connections/ninefour@gdb.sde/GDB.ctgPrimaryFeature"

# Execute Analyze
arcpy.Analyze_management(inDataset, "BUSINESS")