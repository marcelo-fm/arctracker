# Name: ExportReplicaSchema_Example2.py
# Description: Export replica schema from a file geodatabase with a replica

# Import system modules
import arcpy

# Set workspace
arcpy.env.worksapce = "C:/Data"

# Set local variables
replica_workspace = "Countries.gdb"
output_file = "replicaSchema.xml"
replica = "MyReplica1"

# Run ExportReplicaSchema
arcpy.management.ExportReplicaSchema(replica_workspace, output_file, replica)