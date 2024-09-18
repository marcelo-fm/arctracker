# Name: DisableAttachments_Example.py
# Description: GDB Attachments are no longer required, so disable
#              attachments on the input dataset

# Import system modules
import arcpy

# Set the geoprocessing workspace to the feature dataset LandRecord
# in the geodatabase City.gdb
arcpy.env.workspace = r"C:\Data\City.gdb\LandRecord"

# Set local variables
input = "Parcels"

# Use DisableAttachments to delete all attachment files from the gdb
# and disable attachment handling
arcpy.DisableAttachments_management(input)