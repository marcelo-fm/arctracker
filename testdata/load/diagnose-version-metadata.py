# Set the necessary product code
import arceditor
 
# Import arcpy module
import arcpy

# Local variables:
input_database = "c:\\myconnections\\productiongdb.sde"
out_log = "c:\\temp\\gdb_diagnose.log"

# Process: Diagnose Version Metadata
arcpy.DiagnoseVersionMetadata_management(input_database, out_log)