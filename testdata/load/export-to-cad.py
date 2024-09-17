# Description: Create an AutoCAD DWG

# Import system modules
import arcpy

# Set local variables
in_features = "C:/data/EditorTutorial.gdb/StudyArea/Buildings"
output_type = "DWG_R2010"
output_file = "c:/data/Buildings.dwg"

# Process: Export to CAD
arcpy.conversion.ExportCAD(in_features, output_type, output_file, 
                           "USE_FILENAMES_IN_TABLES", "OVERWRITE_EXISTING_FILES")