# Name: SharePackageExample.py
# Description:  Find all map packages that reside in a specified folder 
#               and upload them to the active portal.

# import system modules
import os
import arcpy

# Set environment settings
arcpy.env.overwriteOutput = True
arcpy.env.workspace = "C:/data/my_packages" 

# Loop through the workspace to find all map packages 
for mpkx in arcpy.ListFiles("*.mpkx"):
    print("Uploading " + mpkx)
    arcpy.management.SharePackage(mpkx, "", "", 
                                  "My Summary", "tag1, tag2", 
                                  "My Credits", "MYGROUPS", "My Group")