# Name: ConvertTimeField_Ex02.py
# Description: Convert a time field to date field
# Requirements: None

# Import system modules
import arcpy

# Set local variables
inTable = "C:\Data\TemporalData.gdb\Input_Table"
inputTimeField = "Input_Time"
inputTimeFormat = "1033;MMMM dd, yyyy HH:mm:ss;AM;PM"
outputDateField = "Output_Time"

# Execute CalculateEndDate
arcpy.ConvertTimeField_management(inTable, inputTimeField, inputTimeFormat, outputDateField)