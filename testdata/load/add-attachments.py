"""
Example: You have a folder of digital photographs of vacant homes; the photos
are named according to the Parcel ID of the house in the picture. Add
these photos to a parcel feature class as attachments.
"""

import arcpy
import os

input = r"C:\Data\City.gdb\Parcels"
inputField = "ParcelID"
matchTable = r"C:\Data\matchtable.csv"
matchField = "ParcelID"
pathField = "Picture" 
picFolder = r"C:\Pictures"

# Create a Match Table csv file
with open(matchTable, "w") as csv:
    # write a header row (the table will have two columns: ParcelID and Picture)
    csv.write(f"{matchField},{pathField}\n")
    
    # Iterate through each picture in the directory and write a row to the table
    for file in os.listdir(picFolder):
        if file.find(".jpg") > -1:
            csv.write(f"{file.replace('.jpg', '')},{file}\n")

# The input feature class must first have GDB attachments enabled
arcpy.management.EnableAttachments(input)

# Use the match table with the Add Attachments tool
arcpy.management.AddAttachments(input, inputField, matchTable, matchField, 
                                pathField, picFolder)