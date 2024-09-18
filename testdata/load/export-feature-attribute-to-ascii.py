# Export feature locations and attributes to an ASCII text file
 
# Import system modules
import arcpy
 
# Local variables...
workspace = "c:/data"
input_features = "AidsByCaCnty.shp"
export_ASCII = "aidsbycacnty.txt"

# Set the current workspace (to avoid having to specify the full path to the 
# feature classes each time)
arcpy.env.workspace = workspace

# Process: Export Feature Attribute to ASCII...
arcpy.ExportXYv_stats(input_features, "HEPRATE", "SPACE", export_ASCII, 
                      "NO_FIELD_NAMES")