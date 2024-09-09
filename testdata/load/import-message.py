# Name: ImportMessage_Example3.py
# Description: Import an acknowledgement message into a replica workspace.  

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data"

# Set local variables
replica_workspace = "MySDEdata.sde"
in_message = "acknowledgement.xml" # Acknowledgement file 
output_acknowledgement = "" 	# not applicable when importing an acknowledgement file
conflict_policy = ""        	# not applicable when importing an acknowledgement file 
conflict_detection = ""     	# not applicable when importing an acknowledgement file
reconcile = ""              	# not applicable when importing an acknowledgement file

# Run Import Message
arcpy.management.ImportMessage(replica_workspace, dc_Message, 
                               output_acknowledgement, conflict_policy, 
                               conflict_detection, reconcile)