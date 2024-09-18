# Name: CalculateEndTime_Ex02.py
# Description: Calculate end time based on a start time field
# Requirements: None

# Import system modules
import arcpy

# Set local variables
inTable = "C:/Data/TemporalData.gdb/CalculateEndTime"
uniqueIdFields = ""
startTimeField = "Start_Time"
endTimeField = "End_Time"
 
# Execute CalculateEndDate
arcpy.CalculateEndTime_management(inTable, startTimeField, endTimeField, uniqueIdFields)