"""
Name: GeoTaggedPhotosToPoints example
Description: Find the points that match photo time stamps, then join the output table 
             to the input to see which photos match which points
""" 

# Import system modules
import arcpy
 
# Set environment settings
arcpy.env.workspace = "C:/data"
 
# Set local variables
inFolder = "photos"
inFC = "city.gdb/gps_points"
timeField = "DateTime"
outTable = "city.gdb/output_table"
outUnmatched = "city.gdb/unmatched_photos"
attachmentsOption = "ADD_ATTACHMENTS"
timeDiff = 0
timeOffset = 20

# Run MatchPhotosToRowsByTime and JoinField
arcpy.management.MatchPhotosToRowsByTime(inFolder, inFC, timeField, outTable, 
                                         outUnmatched, attachmentsOption, 
                                         timeDiff, timeOffset)
arcpy.management.JoinField(inFC, "OBJECTID", outTable, "IN_FID", 
                           ["Photo_Path", "Photo_Name", "Match_Diff"])