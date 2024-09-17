# Name: TruncateTable_Example2.py
# Description: Truncates all tables in a file geodatabase.

# Import system modules
import arcpy

# Set the workspace.
arcpy.env.workspace = "C:/work/vancouver.gdb"

# Get a list of all the tables.
tableList = arcpy.ListTables()

# Loop through the list and run truncate
for table in tableList:
    arcpy.TruncateTable_management(table)