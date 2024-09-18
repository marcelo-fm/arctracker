# Description: Delete rows from a table based on an expression
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
inTable = "accident.dbf"
outTable = "C:/output/new_accident.dbf"
tempTableView = "accidentTableView"
expression = arcpy.AddFieldDelimiters(tempTableView, "Measure") + " = 0"
 
# Run CopyRows to make a new copy of the table
arcpy.management.CopyRows(inTable, outTable)

# Run MakeTableView
arcpy.management.MakeTableView(outTable, tempTableView)

# Run SelectLayerByAttribute to determine which rows to delete
arcpy.management.SelectLayerByAttribute(tempTableView, "NEW_SELECTION", 
                                        expression)

# Run GetCount and if some features have been selected, run
#  DeleteRows to remove the selected rows.
if int(arcpy.management.GetCount(tempTableView)[0]) > 0:
    arcpy.management.DeleteRows(tempTableView)