# Name: ExportDataChangesMessage_Example2.py
# Description: Export a data change message to a delta file geodatabase (.gdb).

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
in_geodatabase = "MySDEdata.sde"
out_dataChanges = "Changes.gdb"
replica_name = "MyReplica1"
switch_directions = "SWITCH"
acknowledge = "TRUE"
new_changes = "TRUE"

# Run ExportDataChangeMessage
arcpy.management.ExportDataChangeMessage(in_geodatabase, out_dataChanges, 
                                         replica_name, switch_directions, 
                                         acknowledge, new_changes)