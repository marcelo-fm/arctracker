# Name: ConsolidateToolboxEx2.py
# Description: Find all the toolboxes that reside in a specified folder and 
#              create a consolidated folder for each.

# import system modules
import os
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/Toolboxes"

# Loop through the workspace, find all the toolboxes (.tbx), and create a 
# consolidated folder for each toolbox found using the same name as the original 
# toolbox.
for tbx in arcpy.ListFiles("*.tbx"):
    print("Consolidating " +  tbx)
    arcpy.management.ConsolidateToolbox(tbx, os.path.splitext(tbx)[0], "CURRENT")