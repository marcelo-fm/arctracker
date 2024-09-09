# Name: ExportAcknowledgement_Example2.py
# Description: Exports an acknowledgement message from a replica geodatabase (SDE).

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
in_geodatabase = "MySDEdata.sde"
output_file = "AcknowledgementMessage.xml"
replica_name = "MyReplica1"
arcpy.management.ExportAcknowledgementMessage(in_geodatabase, output_file , replica_name)