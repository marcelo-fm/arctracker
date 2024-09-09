# Name: CalculateLineCaps_standalone_script.py
# Description: Calculates the cap type for stroke symbol layers in the line 
#              symbols of the input layer
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "roads.lyrx"
cap_type = "BUTT"
dangle_option = "CASED_LINE_DANGLE"

# Execute Calculate Line Caps
arcpy.CalculateLineCaps_cartography(in_features, cap_type, dangle_option)