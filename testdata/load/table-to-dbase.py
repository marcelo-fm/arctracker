# Name: TableToDBASE_Example2.py
# Description: Use TableToDBASE to copy tables to dBASE format
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inTables = ["vegtype", "futrds"]
outLocation = "C:/output"

# Run TableToDBASE
arcpy.conversion.TableToDBASE(inTables, outLocation)