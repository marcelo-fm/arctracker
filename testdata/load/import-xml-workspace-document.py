# Name: ImportXMLWorkspaceDocument.py
# Description: Import the contents of an XML workspace document into a target 
#              geodatabase. 

# Import system modules
import arcpy

# Set local variables
target_gdb = "c:/data/Target.gdb"
in_file = "c:/data/StJohnsData.xml"
import_type = "SCHEMA_ONLY"
config_keyword = "DEFAULTS"

# Execute ImportXMLWorkspaceDocument
arcpy.ImportXMLWorkspaceDocument_management(target_gdb, in_file, import_type, 
                                            config_keyword)