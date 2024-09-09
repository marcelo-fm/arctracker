# Name: GenerateLicensedFileGeodatabase.py
# Description: Use the GenerateLicensedFgdb tool to license a file geodatabase

# import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
geodatabase = "london.gdb"
out_geodatabase = "london_lic.gdb"
licdef = "london.licdef"

# Process: Restrict the data
arcpy.management.GenerateFgdbLicense(geodatabase, out_geodatabase, licdef)