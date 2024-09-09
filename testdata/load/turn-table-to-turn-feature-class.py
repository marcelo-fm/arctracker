# Name: TurnTableToTurnFeatureClass_ex03.py
# Description: Converts a Arcview 3.x turn table to a turn feature class
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env

#Set environment settings
env.workspace = "C:/data/SanFrancisco.gdb/Transportation"

#Set local variables
inTurnTable = "C:/data/DelayTurns.dbf"
refLineFeatures = "Streets"
outTurnFeatureClassName = "DelayTurns"
maxEdges = 7

#Convert the ArcView 3.x Turn table to geodatabase turn feature class
#The streets shapefile referred by the turn features has been converted to a
#feature class in the geodatabase.
arcpy.TurnTableToTurnFeatureClass_na(inTurnTable, refLineFeatures,
                                     outTurnFeatureClassName, "", maxEdges)

print("Script completed successfully.")