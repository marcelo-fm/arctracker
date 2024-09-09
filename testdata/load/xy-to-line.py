# Import system modules
import arcpy

# Set local variables
input_table = r"c:\workspace\city2city.dbf"
out_lines = r"c:\workspace\flt4421.gdb\routing001"

# XY To Line
arcpy.XYToLine_management(input_table, out_lines, "LOND1", "LATD1", "LOND2",
                          "LATD2", "GEODESIC", "idnum")