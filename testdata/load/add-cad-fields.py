# Import system modules
import arcpy

# Set workspace
arcpy.env.workspace = "C:/data"

# Set local variables
input_table = "C:/data/EditorTutorial.gdb/StudyArea/Buildings"

# Process: Add CAD Fields
arcpy.conversion.AddCADFields(input_table, "ADD_ENTITY_PROPERTIES", 
                              "ADD_LAYER_PROPERTIES", "NO_TEXT_PROPERTIES",
                              "NO_DOCUMENT_PROPERTIES", "NO_XDATA_PROPERTIES")