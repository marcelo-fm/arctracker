# Name: ThinRoadNetwork_standalone_script.py
# Description:  Removes a subset of road segments to create a simplified road 
#               network that retains the connectivity and character of the 
#               input.
 
# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"

# Set local variables
in_features = "roads.lyrx"
minimum_length = "1000 meters"
invisibility_field = "invisible"
level_field = "level"

# Execute Thin Road Network
arcpy.ThinRoadNetwork_cartography(in_features, minimum_length, 
                                  invisibility_field, level_field)