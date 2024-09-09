# Name: DisperseMarkers_standalone_script.py
# Description: Finds point symbols that are overlapping or too close to one 
#              another and spreads them apart based on a minimum spacing and 
#              dispersal pattern

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
arcpy.env.referenceScale = "50000"

# Set local variables
in_point_features = "crime.lyrx"
minimum_spacing = "2 Points"
dispersal_pattern = "EXPANDED"

# Execute Disperse Markers
arcpy.DisperseMarkers_cartography(in_point_features, minimum_spacing, 
                                  dispersal_pattern)