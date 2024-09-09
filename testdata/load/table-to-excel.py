import arcpy

# Set environment settings
arcpy.env.workspace = "c:/data"

# Set local variables
in_table = "gdb.gdb/addresses"
out_xls = "addresses.xls"

# Run TableToExcel
arcpy.conversion.TableToExcel(in_table, out_xls)