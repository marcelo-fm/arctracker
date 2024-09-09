# Set the necessary product code
import arceditor

# Import arcpy module
import arcpy

# Local variables:
schema_gdb = "usr/connections/land@ora11204.sde"

# Process: Delete Schema Geodatabase
arcpy.management.DeleteSchemaGeodatabase(schema_gdb)