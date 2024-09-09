# Set the necessary product code
import arceditor
 
# Import arcpy module
import arcpy

# Local variables:
ent_gdb = "C:\\gdbs\\enterprisegdb.sde"
output_file = "C:\\temp\\keyword.txt"

# Process: Export configuration keywords to a text file
arcpy.ExportGeodatabaseConfigurationKeywords_management(ent_gdb,output_file)