# Name: CreateReplicaFromServer_Example2.py
# Description: Creates a two-way replica from a geodata service

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data/MySDEdata.sde"

# Set local variables
gisServer = "C:/MyServerConn/RoadMap.GeodataServer"
in_datasets = "Roads; Streets"
replica_type = "TWO_WAY_REPLICA"
out_workspace = env.workspace
replica_name = "MajorRoads_replica"
access_type = "FULL"
initial_sender = "CHILD_DATA_SENDER"
expand = "USE_DEFAULTS"
reUse = "DO_NOT_REUSE"
related = "GET_RELATED"
replica_geometry = "LA_County"
archiving = "DO_NOT_USE_ARCHIVING"

# Run CreateReplicaFromServer
arcpy.management.CreateReplicaFromServer(
        gisServer, in_datasets, replica_type, out_workspace, replica_name, 
        access_type, initial_sender, expand, reUse, related, replica_geometry, 
        archiving)