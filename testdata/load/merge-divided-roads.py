# Name: MergeDividedRoads_standalone_script.py
# Description: Resolves symbology conflicts between roads within
#              a specified distance of each other by snapping them together

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "C:/data"
arcpy.env.referenceScale = "50000"

# Set local variables
in_features = "roads.lyrx"
merge_field = "level"
collapse_distance = "25 meters"
out_features = "cartography.gdb/transportation/merged_roads"
out_displacement_features = "cartography.gdb/transportation/displacement"
out_table = "cartography.gdb/outtable_tbl"

# Execute Merge Divided Roads
arcpy.cartography.MergeDividedRoads(in_features, merge_field,
                                    collapse_distance, out_features,
                                    out_displacement_features, out_table)