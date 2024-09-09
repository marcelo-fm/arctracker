# Name: FindOverlaps_Example2.py
# Description: Find overlaps/intersections of polygons.

# Import system modules
import arcpy

# Set local variables
in_features = "C:/data/input.gdb/areas" 
out_intersections = "C:/data/results.gdb/intersections"
out_centroids = "C:/data/results.gdb/centroids" 
group_field = "category"

# Run FindOverlaps
arcpy.intelligence.FindOverlaps(in_features, out_intersections,
                                out_centroids, group_field)