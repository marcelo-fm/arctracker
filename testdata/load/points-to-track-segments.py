# Name: PointsToTrackSegments_Example2.py
# Description: Convert points to track segments.

# Import system modules
import arcpy 

# Set local variables
in_features = "C:/data/mtracks.gdb/source_pts"
date_time = "DateTime"
out_feature_class = "C:/data/mtracks.gdb/tracklines"
group_field = "Name" 
out_points = "C:/data/mtracks.gdb/seqpoints"

# Run PointsToTrackSegments
arcpy.intelligence.PointsToTrackSegments(in_features, date_time, 
                                         out_feature_class, group_field,
                                         "INCLUDE_VELOCITY", out_points)