#  Description: Use TableToTable with an expression to create a subset
#  of the original table.
 
# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inTable = "vegtable.dbf"
outTable = "C:/output/output.gdb/estuarine.csv"

# Set the expression, with help from the AddFieldDelimiters function, to select 
# the appropriate field delimiters for the data type
expression = arcpy.AddFieldDelimiters(arcpy.env.workspace, "VEG_TYPE") + " = 'Estuarine'"
 
# Run TableToTable
arcpy.conversion.ExportTable(inTable, outTable, expression, "NOT_USE_ALIAS")