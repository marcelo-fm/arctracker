# Set the necessary product code
import arceditor
 
# Import arcpy module
import arcpy

# Local variables:
ent_gdb = "C:\\gdbs\\enterprisegdb.sde"
input_file = "C:\\temp\\keyword.txt"

# Process: Import the text file containing configuration keywords
arcpy.ImportGeodatabaseConfigurationKeywords_management(ent_gdb,input_file)