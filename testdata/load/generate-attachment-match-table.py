# Name: GenerateAttachmentMatchTable_Example.py
# Description: Create an attachment match table for all files that contain the string
# 'property' and are of type 'jpg' while looping through multiple folders.

# Import system modules
import arcpy
import os

# Set local variables.
rootFolder = 'c:/work/'

for folder in os.walk(rootFolder):
    # Exclude file geodatabases from the folder list.
    if folder[0].find('.gdb') == -1:
        arcpy.management.GenerateAttachmentMatchTable(
            "C:/data/parcels.gdb/parcels", folder[0], 
            "C:/data/temp.gdb/matchtable", "AttachmentKeyField", 
            "*property*.jpg", "RELATIVE", "EXACT")