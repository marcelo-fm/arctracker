# Name: CreateTurnFeatureClass_ex03.py
# Description: Create a new turn feature class associated with a network dataset
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env

#Set environment settings
env.workspace = "C:/data/SanFrancisco.gdb"

#Set local variables
inFeatureDataset = "Transportation"
outTurnFeatureClassName = "DelayTurns"
maxEdges = 3
inNetworkDataset = inFeatureDataset + "/" + "Streets_ND"

#Create a turn feature class and add it as a turn source by specifying the
#network dataset
arcpy.CreateTurnFeatureClass_na(inFeatureDataset,outTurnFeatureClassName,
                                maxEdges, inNetworkDataset)

print("Script completed successfully.")