"""
Example: You have a folder of digital photographs of vacant homes; the photos
         are named according to the ParcelID of the house in the picture. You'll 
         add these photos to a parcel feature class as attachments.
"""

import csv
import arcpy
import os

input = r"C:\Data\City.gdb\Parcels"
inputField = "ParcelID"
matchTable = r"C:\Data\matchtable.csv"
matchField = "ParcelID"
pathField = "Picture" 
picFolder = r"C:\Pictures"

# Create a new Match Table .csv file
writer = csv.writer(open(matchTable, "wb"), delimiter=",")

# Write a header row (the table will have two columns: ParcelID and Picture)
writer.writerow([matchField, pathField])

# Iterate through each picture in the directory and write a row to the table
for file in os.listdir(picFolder):
    if str(file).find(".jpg") > -1:
        writer.writerow([str(file).replace(".jpg", ""), file])

del writer

# The input feature class must first be GDB attachments enabled
arcpy.EnableAttachments_management(input)

# Use the match table with the Add Attachments tool
arcpy.AddAttachments_management(input, inputField, matchTable, matchField, 
                                pathField, picFolder)