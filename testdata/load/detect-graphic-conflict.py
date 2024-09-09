# Name: DetectGraphicConflict_standalone_script.py
# Description: Detects graphic conflicts between
#              feature representations and stores
#              the overlaps as polygons in
#              the output feature class.
# Author: ESRI
 
# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "C:/data/cartography.gdb/buildings"
env.referenceScale = "50000"

# Set local variables
in_features = "footprints.lyr"
conflict_features = "roads.lyr"
out_feature_class = "C:/data/carto.gdb/buildings/dgc_polys"
conflict_distance = "25 meters"
line_connection_allowance = "0 meters"

# Execute Detect Graphic Conflict
arcpy.DetectGraphicConflict(in_features,
                            conflict_features,
                            out_feature_class,
                            conflict_distance,
                            line_connection_allowance)