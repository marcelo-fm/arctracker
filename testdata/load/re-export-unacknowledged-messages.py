# Name: ReExportUnacknowledgedMessages_Example2.py
# Description: Reexport all unacknowledged messages from an SDE replica workspace.
# Changes are exported to a delta geodatabase

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
replica_gdb = "MySDEdata.sde"
output_file = "dataChanges2.gdb"
replica_name = "MyReplica1"
export_option = "ALL_UNACKNOWLEDGED"

# Run ReExportUnacknowledgedMessages
arcpy.management.ReExportUnacknowledgedMessages(replica_gdb, output_file, 
                                                replica_name, export_option)