# Name: CreateReplica_Example2.py
# Description: Create a one-way replica of a Feature Dataset to a file geodatabase. 

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data/MyData.sde"

# Set local variables
in_data = "Parks" # a feature dataset
replica_type = "ONE_WAY_REPLICA"
output_workspace = "C:\Data\MyTargetGDB.gdb"
replica_name = "MyReplica"
access_type = "FULL"
initial_sender = "PARENT_DATA_SENDER"
expand = "USE_DEFAULTS"
reuse_schema = "DO_NOT_REUSE"
get_related = "GET_RELATED"
replica_geometry = "LA_County"
archiving = "DO_NOT_USE_ARCHIVING"

# Run CreateReplica
arcpy.management.CreateReplica(in_data, replica_type, output_workspace, 
                               replica_name, access_type, initial_sender, 
                               expand, reuse_schema, get_related, 
                               replica_geometry, archiving)