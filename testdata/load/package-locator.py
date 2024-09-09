# Name: PackageLocatorEx.py
# Description:  Find all the locators that reside in a specified folder and 
#               create a locator package for each locator.

# import system modules
import os
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/MyData/Locators" 

# Loop through the workspace, find all the locators, and create a locator package 
# using the same name as the locator.
for loc in arcpy.ListFiles("*.loc"):
    print("Packaging " + loc)
    arcpy.PackageLocator_management(loc, os.path.splitext(loc)[0] + '.gcpk', "", 
                                    "#", "Summary of package","tag1; tag2; tag3")