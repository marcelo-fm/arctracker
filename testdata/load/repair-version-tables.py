# Description: repair version metadata

# Set the necessary product code
import arceditor
 
# Import arcpy module
import arcpy

# Local variables:
input_database = "c:\\temp\\productiongdb.sde"
out_log = "c:\\temp\\gdb_repair.log"
target_version = "SDE.Default"
input_tables = "GIS.Parcels"

# Process: Repair Version Metadata
arcpy.RepairVersionMetadata_management(input_database, out_log, target_version, 
                                       input_tables)