# Name: UpdateByGeometry_ex02.py
# Description: Update edge references in the turn feature class using the
#              geometry of turn features and re-build the network dataset.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env

#Set environment settings
env.workspace = "C:/data/SanFrancisco.gdb"

#Set local variables
inTurnFeatures = "RestrictedTurns"
inNetworkDataset = "Transportation/Streets_ND"

#update the edge references in turn features using the geometry
arcpy.UpdateByGeometry_na(inTurnFeatures)

#Since we have modified the edge references for turn sources, we should rebuild
#the network dataset so that the turn features are correctly interpreted by the
#network dataset
arcpy.BuildNetwork_na(inNetworkDataset)

print("Script completed successfully.")