# Name: PivotTable_Example2.py
# Description: Pivot the attributes table by the specified fields

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
in_table = "attributes.dbf"
fields = "OwnerID"
pivot_field = "AttrTagNam"
value_field = "AttrValueS"
out_table = "C:/output/attribPivot.dbf"

# Run PivotTable
arcpy.management.PivotTable(in_table, fields, pivot_field, value_field, out_table)