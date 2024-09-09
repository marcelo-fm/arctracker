# Description: Use TableToTable with an expression to create a subset
#  of the original table.
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inTable = "vegtable.dbf"
outLocation = "C:/output/output.gdb"
outTable = "estuarine"

# Set the expression, with help from the AddFieldDelimiters function, to select 
# the appropriate field delimiters for the data type
expression = arcpy.AddFieldDelimiters(arcpy.env.workspace, "VEG_TYPE") + " = 'Estuarine'"
 
# Run TableToTable
arcpy.conversion.TableToTable(inTable, outLocation, outTable, expression)