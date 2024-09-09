# Description: Convert all dBASE tables in a folder to geodatabase tables
# Requirement: os module

# Import system modules
import arcpy
import os
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
outWorkspace = "c:/output/output.gdb"
 
# Use ListTables to generate a list of dBASE tables in the
#  workspace shown above.
tableList = arcpy.ListTables()
 
# Run CopyRows for each input table
for dbaseTable in tableList:
    # Determine the new output feature class path and name
    outTable = os.path.join(outWorkspace, os.path.splitext(dbaseTable)[0])
    arcpy.management.CopyRows(dbaseTable, outTable)