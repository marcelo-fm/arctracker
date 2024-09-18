import arcpy

# Import system variables
import arcpy

# Set the workspace
arcpy.env.workspace = r"C:\National.gdb"

# Set local variables
in_dataset = "Airports"
out_location = r"C:\Output_Images"
subdir_field = 'Code'
output_names = 'REPLACE'
name_fields = ['NAME', 'CODE']

# Select the Salt Lake City Airport and download all attachments to a subdirectory named SLC.
layerSelection = arcpy.management.SelectLayerByAttribute(in_dataset, 'NEW_SELECTION',
                                                         "Name = 'Salt Lake City'")

# Export the attachments with the layer selection set and renamed using field values.
arcpy.management.ExportAttachments(layerSelection, out_location, subdir_field,
                                   output_names, name_fields)