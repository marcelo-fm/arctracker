# Name: ExportXMLWorkspaceDocument.py
# Description: Export the contents of my geodatabase to an XML workspace document. 

# Import system modules
import arcpy

# Set local variables
in_data = 'c:/data/StJohns.gdb'
out_file = 'c:/data/StJohns.xml'
export_option = 'SCHEMA_ONLY'
storage_type = 'BINARY'
export_metadata = 'METADATA'

# Run ExportXMLWorkspaceDocument
arcpy.management.ExportXMLWorkspaceDocument(in_data, out_file, export_option, 
                                            storage_type, export_metadata)