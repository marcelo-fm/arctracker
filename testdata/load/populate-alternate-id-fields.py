# Name: PopulateAlternateIDFields_ex02.py
# Description: Create and populate the alternate ID fields for all turn sources
#              in the network dataset.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env

#Set environment settings
env.workspace = "C:/data/SanFrancisco.gdb/Transportation"

#Set local variables
inNetworkDataset = "Streets_ND"
altIDFieldName = "ID"

#Populate alternate IDs on all turn sources in the network dataset
arcpy.PopulateAlternateIDFields_na(inNetworkDataset,altIDFieldName)

print("Script completed successfully.")