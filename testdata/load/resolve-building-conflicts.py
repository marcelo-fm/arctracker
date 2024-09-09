# Name: ResolveBuildingConflicts_standalone_script.py
# Description: Resolves the symbology conflicts between
#              buildings and nearby barriers,
#              in this case - roads
 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"
env.referenceScale = "50000"

# Set local variables
in_buildings = "C:/data/footprints.lyr;C:/data/bldg_pts.lyr"
invisibility_field = "invisible"
in_barriers = "'C:/data/roads.lyr' 'true' '5 Meters';\
              'C:/data/trails.lyr' 'false' '10 Meters';\
              'C:/data/streams.lyr' 'false' '5 Meters'"
building_gap = "10 meters"
minimum_size = "15 meters"
hierarchy_field = "bldg_hierarchy"

# Execute Resolve Building Conflicts
arcpy.ResolveBuildingConflicts(in_buildings,
                               invisibility_field,
                               in_barriers,
                               building_gap,
                               minimum_size,
                               hierarchy_field)