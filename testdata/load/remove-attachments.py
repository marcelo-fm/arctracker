# Delete unnecessary attachments from a feature class

import arcpy
import csv

input = r"C:\Data\City.gdb\Parcels"
inputField = "ParcelID"
matchTable = r"C:\Data\matchtable.csv"
matchField = "ParcelID"
nameField = "Picture" 

# Create a new Match Table csv file that will tell the RemoveAttachments tool 
# which attachments to delete.
writer = csv.writer(open(matchTable, "wb"), delimiter=",")

# Write a header row (the table will have two columns: ParcelID and Picture)
writer.writerow([matchField, nameField])

# Create a list of the attachments to delete.
# Removes attachments pic1a.jpg and pic1b.jpg from feature 1, pic3.jpg from 
# feature 3, and pic4.jpg from feature 4.
deleteList = [[1, "pic1a.jpg"], [1, "pic1b.jpg"], [3, "pic3.jpg"], [4, "pic4.jpg"]]

# Iterate through the delete list and write it to the Match Table csv.
for row in deleteList:
    writer.writerow(row)

del writer

# Use the match table with the Remove Attachments tool.
arcpy.RemoveAttachments_management(input, inputField, matchTable, matchField, 
                                   nameField)