# Name: calculatecentralmeridianandparallels_example.py
# Description: Calculates the central meridian and optional standard parallels
# for a set of features
# Author: ESRI

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
arcpy.env.workspace = "C:\Data\ProjectData.gdb"

# Set local variables
inFeatures = "US_states"
coordsysField = "CentralMeridian"
standardOffset = 0.25

# Execute CalculateAdjacentFields
arcpy.CalculateCentralMeridianAndParallels_cartography(inFeatures,
                                                       coordsysField,
                                                       standardOffset)