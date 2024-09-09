# Name: ConvertTimeZone_Ex02.py
# Description: Convert a time field to another time zone
# Requirements: None

# Import system modules
import arcpy

# Set local variables
inTable = "C:/Data/TemporalData.gdb/InputData"
inputTimeField = "Input_Time"
inputTimeZone = "Pacific_Standard_Time"

outputTimeField = "Output_Time"
onputTimeZone = "Eastern_Standard_Time"
inputUseDaylightSaving = "INPUT_ADJUSTED_FOR_DST"
outputUseDaylightSaving = "OUTPUT_ADJUSTED_FOR_DST"

# Execute CalculateEndDate
arcpy.ConvertTimeZone_management(inTable, inputTimeField, inputTimeZone, outputTimeField, onputTimeZone, inputUseDaylightSaving, outputUseDaylightSaving)