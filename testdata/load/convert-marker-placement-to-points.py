# Name: ConvertMarkerPlacementToPoints_standalone_script.py
# Description: Converts markers in a marker placement into point features.

# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"
env.referenceScale = "5000"

# Set local variables
in_layer = "parks.lyrx"
out_feature_class = "cartography.gdb/tree_markers"
create_multipoints = "CREATE_MULTIPOINTS"
boundary_option = "VALUE_FROM_FIELD"
boundary_distance = ""
boundary_distance_field = "distance"
boundary_distance_unit = "Points"
in_barriers = [["roads.lyrx", 1, "", "Points"],["rivers.lyrx", 0, "distance", "Points"]]
keep_at_least_one_marker = "KEEP_AT_LEAST_ONE_MARKER"
displacement_method = "DISPLACE_APART"
minimum_marker_distance = "2 Points"


arcpy.cartography.ConvertMarkerPlacementToPoints(in_layer,
                                                 out_feature_class,
                                                 create_multipoints,
                                                 boundary_option,
                                                 boundary_distance,
                                                 boundary_distance_field,
                                                 boundary_distance_unit,
                                                 in_barriers,
                                                 keep_at_least_one_marker,
                                                 displacement_method,
                                                 minimum_marker_distance
)