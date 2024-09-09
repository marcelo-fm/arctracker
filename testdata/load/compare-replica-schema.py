# Description: Compare a replica schema (in an enterprise geodatabase 
#              workspace) to its relative replicas schema (in an .xml file).
#              The results of the comparison are created in an .xml file.
#              The relative replica's .xml schema file was created using the 
#              ExportReplicaSchema function.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
in_geodatabase = "MySDEdata.sde"
in_source_file = "RelativeReplicaSchema.xml"
output_schema_changes = "outputSchemaChanges.xml"

# Run CompareReplicaSchema
arcpy.management.CompareReplicaSchema(in_geodatabase, in_source_file, output_schema_changes)