# Set the necessary product code
import arceditor
 
# Import arcpy module
import arcpy

# Local variables:
input_database = "c:\\myconnections\\productiongdb.sde"
out_log = "c:\\temp\\gdb_repair.log"

# Process: Repair Version Metadata
arcpy.RepairVersionMetadata_management(input_database, out_log)