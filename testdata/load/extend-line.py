# Name: ExtendLine.py
# Description:  Clean up street centerlines that were digitized without 
#               having set proper snapping environments.

# import system modules 
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Make backup copy of streets feature class, since modification with 
#  the Editing tools below is permanent
streets = "majorrds.shp"
streetsBackup = "C:/output/Output.gdb/streetsBackup"
arcpy.management.CopyFeatures(streets, streetsBackup)

# Trim street lines to clean up dangles
arcpy.edit.TrimLine(streets, "10 Feet", "KEEP_SHORT")

# Extend street lines to clean up dangles
arcpy.edit.ExtendLine(streets, "15 Feet", "EXTENSION")