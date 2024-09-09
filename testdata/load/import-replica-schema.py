# Description: Import a schema changes file into a replica geodatabase

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
replica_geodatabase = "Countries.gdb"
schema_file = "schemaDifferences.xml"

# Run ImportReplicaSchema
arcpy.management.ImportReplicaSchema(replica_geodatabase, schema_file)