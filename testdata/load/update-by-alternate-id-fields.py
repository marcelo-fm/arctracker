# Name: UpdateByAlternateIDFields_ex02.py
# Description: Update the edge references in the turn feature classes using
#              alternate IDs and build the network dataset.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env

#Set environment settings
env.workspace = "C:/data/SanFrancisco.gdb"

#Set local variables
inNetworkDataset = "Transportation/Streets_ND"
altIDFieldName = "ID"

#Update the edge references in the turn features using alternate ID fields
arcpy.UpdateByAlternateIDFields_na(inNetworkDataset, altIDFieldName)

#Since we have modified the edge references for turn sources, we should rebuild
#the network dataset so that the turn features are correctly interpreted by the
#network dataset
arcpy.BuildNetwork_na(inNetworkDataset)

print("Script completed successfully.")