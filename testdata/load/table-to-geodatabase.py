# Name: TableToGeodatabase_Example2.py
# Description: Use TableToDBASE to copy tables to geodatabase format
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"

# Make list of all tables in workspace
# The list of tables should be similar to this: 
#  ["accident.dbf", "vegtable.dbf"]
tables = arcpy.ListTables()

# Set local variables
outLocation = "C:/output/output.gdb"

# Run TableToGeodatabase
print(f"Importing tables to gdb: {outLocation}")
arcpy.conversion.TableToGeodatabase(tables, outLocation)