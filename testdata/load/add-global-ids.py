# Name: AddGlobalIDs_Example2.py
# Description: Add globalIDs to a list of datasets. Both feature classes are in the same enterprise workspace.

# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/Data/MySDEdata.sde"

# Set local variables
in_dataset1 = "GDB1.Heather.Roads"
in_dataset2 = "GDB1.Heather.Streets"

# Run AddGlobalIDs
arcpy.management.AddGlobalIDs([in_dataset1, in_dataset2])