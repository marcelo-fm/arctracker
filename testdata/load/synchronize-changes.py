# Name: SynchronizeChanges_Example2.py
# Description: Synchronizes changes for a one way replica from the Parent to 
#              the child replica geodatabase. The parent is an enterprise 
#              geodatabase workspace, and the child is file geodatabase.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
replica_gdb1 = "MyData.sde"
replica_gdb2 = "Counties_replica.gdb"
replica_name = "MyOneWayReplica"
sync_direction = "FROM_GEODATABASE1_TO_2"
conflict_policy = ""     # Not applicable for one way replicas, there is not conflict detection.
conflict_detection = ""  # Not applicable for one way replicas, there is not conflict detection.
reconcile = ""           # Only applicable for Checkout replicas

# Execute SynchronizeChanges
arcpy.SynchronizeChanges_management(replica_gdb1, replica_name, replica_gdb2, 
                                    sync_direction, conflict_policy, 
                                    conflict_detection, reconcile)