# Name: ConsolidateLocator.py
# Description:  Find all the locators that reside in a specified folder and create a consolidated folder for each locator.

# import system modules
import os
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/MyData/Locators"

# Loop through the workspace, find all the loc and create a consolidated folder using the same 
# name as the original locator
for loc in arcpy.ListFiles("*.loc"):
    print("Consolidating " + loc)
    arcpy.ConsolidateLocator_Management(loc, os.path.splitext(loc)[0])