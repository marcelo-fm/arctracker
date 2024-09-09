# Name: ExtractPackage.py
# Description: Find geoprocessing packages in a specified folder and extract 
#              contents.

import arcpy
import os

arcpy.env.overwriteOutput = True

# set folder that contains packages to extract
arcpy.env.workspace = "C:/geoprocessing/gpks" 
wrksp = arcpy.env.workspace

for gpk in arcpy.ListFiles("*.gpk"):
    print("Extracting... " + gpk)
    arcpy.management.ExtractPackage(gpk, os.path.splitext(gpk)[0])

print("done")