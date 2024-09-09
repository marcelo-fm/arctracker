# Name: IncreaseMaximumEdges_ex02.py
# Description: Increase maximum edges for turn features from 2 to 5.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env

#Set environment settings
env.workspace = "C:/data/SanFrancisco.gdb/Transportation"

#Set local variables
inTurnFeatures = "RestrictedTurns"
maxEdges = 5

#Increase the edges for turn features
arcpy.IncreaseMaximumEdges_na(inTurnFeatures, maxEdges)

print("Script completed successfully.")