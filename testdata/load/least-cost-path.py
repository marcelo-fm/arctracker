# Name: LeastCostPath_Example2.py
# Description: Generate the least cost path between an input and output point 
#              based on a cost surface.

# Import system modules
import arcpy
import os

# Set local variables
in_cost_surface = r"c:\workspace\terrain.gdb\mob_cost_surf" 
in_start_point = r"c:\workspace\startinglocation.shp" 
in_end_point = r"c:\workspace\endinglocation.shp"
out_path_feature_class = os.path.join(arcpy.env.scratchWorkspace, "bestpath")
handle_zeros = "SMALL_POSITIVE"

# Run LeastCostPath
arcpy.intelligence.LeastCostPath(in_cost_surface, in_start_point, 
                                 in_end_point, out_path_feature_class,
                                 handle_zeros)

# Report status
if arcpy.Exists(out_path_feature_class): 
    print("Path segments {}".format(arcpy.management.GetCount(out_path_feature_class)[0]))
else: 
    print("Empty output")