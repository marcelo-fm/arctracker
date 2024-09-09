# Name: CreateUnderpass_standalone_script.py
# Description: creates a mask where one feature
#              is visually below another feature
 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data"
env.referenceScale = "50000"

# Set local variables
in_above_features = "roads.lyr"
in_below_features = "railroads.lyr"
margin_along = "2 Points"
margin_across = "1 Points"
out_overpass_feature_class = "cartography.gdb/trans/under_mask_fc"
out_mask_relationship_class = "cartography.gdb/trans/under_mask_rc"
where_clause = "'RelationshipToSurface' = 3"
out_decoration_feature_class = "cartography.gdb/trans/tunnel"
wing_type = "PARALLEL"
wing_tick_length = "1 Points"

# Execute Create Underpass
arcpy.CreateUnderpass_cartography(in_above_features,
                                  in_below_features,
                                  margin_along,
                                  margin_across,
                                  out_overpass_feature_class,
                                  out_mask_relationship_class,
                                  where_clause,
                                  out_decoration_feature_class,
                                  wing_type,
                                  wing_tick_length)