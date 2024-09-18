"""
Name:        SplitLineByMatch_example_script2.py
Description: Use DetectFeatureChanges to get initial matching and then use
             SplitLineByMatch to split the source and target to improve spatial
             correspondence. 
             Finally use TransferAttributes to transfer a field value from the
             split source to the split target features.
"""

# Import system modules
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\conflation\Tools\splitlinebym\roads.gdb"

# Set local variables
sourceFeatures = "sourceRoads"
targetFeatures = "targetRoads"

dfcOutput = "DFC"
searchDistance = "100 Feet"
dfcMatchTable = "DFC_mtable"

slbmSourceOutput = "out_source"
slbmSourceOutputPts = "out_sourcePoints"
slbmTargetOutput = "out_target"
slbmTargetOutputPts = "out_targetPoints"
dangle = "SPLIT_DANGLE"
minSplitLength = "300 Feet"

transfer_fields = "Mile_Length"

# Use Detect Feature Changes tool to generate the needed match table
arcpy.management.DetectFeatureChanges(sourceFeatures, targetFeatures, dfcOutput, searchDistance, dfcMatchTable)

# Use Split Line By Match tool twice to split source and then target features to improve spatial correspondence
arcpy.edit.SplitLineByMatch(sourceFeatures, targetFeatures, dfcMatchTable, slbmSourceOutput, searchDistance,
                            "AS_SOURCE", slbmSourceOutputPts, dangle, "", minSplitLength)

arcpy.edit.SplitLineByMatch(targetFeatures, sourceFeatures, dfcMatchTable, slbmTargetOutput, searchDistance,
                            "AS_TARGET", slbmTargetOutputPts, dangle, "", minSplitLength)

# Perform attribute transfer using the split results
arcpy.edit.TransferAttributes(slbmSourceOutput, slbmTargetOutput, transfer_fields, searchDistance)