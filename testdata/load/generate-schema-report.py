# Name: GenerateSchemaReport_Example.py
# Description: GenerateSchemaReport of a file geodatabase

# Import the system modules
import arcpy

# Set local variables
gdbWorkspace = "C:/data/data.gdb"

arcpy.management.GenerateSchemaReport(gdbWorkspace, "C:/MyProject/My_folder", "schema_report", ["JSON", "PDF"])