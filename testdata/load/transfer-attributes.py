"""
Name:        TransferAttributes_example_script3.py
Description: Perform attribute transfer from newly updated roads (source) to
             existing base roads (target). When the source and target
             features are matched in many-to-one or many-to-many (m:n)
             relationships, attributes can be transferred based on transfer
             rules. This script shows how transfer rules are set.
"""

# Import system modules
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\conflationTools\ScriptExamples\data.gdb"

# Set local variables
sourceFeatures = "updateRoads"
targetFeatures = "baseRoads"
transfer_fields = "RD_NAME"

search_distance = "300 Feet"
match_fields = ""
outMatchTable = ""
transfer_rules = [["TRAVEL_DIRECTION", "One-Way"], ["SPEED_LIMIT", "MAX"]]

# Make a copy of the targetFeatures for attribute transfer
targetCopy = targetFeatures + "_Copy"
arcpy.management.CopyFeatures(targetFeatures, targetCopy)

# Perform attribute transfer
arcpy.edit.TransferAttributes(sourceFeatures, targetCopy, transfer_fields,
                              search_distance, match_fields, outMatchTable,
                              transfer_rules)