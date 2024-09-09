# Name: RecoverFileGeodatabase.py
# Description: Use the RecoverFileGeodatabase tool to recover the data
#              contained in a damaged file geodatabase.

# Import system modules
import arcpy

# Set local variables
geodatabase = "C:/fgdb/Whistler.gdb"
output_location = "C:/recoveredData"
recovered_name = "recoveredWhistler.gdb"

# Process: Recover the data
arcpy.RecoverFileGDB_management(geodatabase, output_location, recovered_name)