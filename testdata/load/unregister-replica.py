# Import modules
import arcpy

# Set local variables
sdeConnection = "C:\\MyProject\\myConnection.sde"

# Loop through all replicas and unregister each one
replicas = arcpy.da.ListReplicas(sdeConnection, True)
for replica in replicas:
    arcpy.management.UnregisterReplica(sdeConnection, replica.name)