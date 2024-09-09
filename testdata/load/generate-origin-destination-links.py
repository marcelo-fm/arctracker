# Name: GenerateODLinks.py
# Description: Finds 10 nearest links within 25 miles from the origin fire
#              stations to the destination response points.

# import system modules
import arcpy

# set workspace environment
arcpy.env.workspace = "C:/data/input/genODLinks.gdb"

# set required parameters 
origin_features = "Station_100"
destination_features = "City_FireResponses"
out_feature_class = "Station_100_OD_Links"

# optional parameters
origin_group_field = 'STA_NUM'
destination_group_field = 'District'
line_type = 'PLANAR'
num_nearest = 10
search_distance = 25
distance_unit = 'MILES'
aggregate_links='AGGREGATE_OVERLAPPING'
sum_fields = 'TimeSpentOnCall SUM'

# make links between fire stations and call response points
arcpy.analysis.GenerateOriginDestinationLinks(
    origin_features, destination_features, out_feature_class,
    origin_group_field, destination_group_field, line_type, num_nearest,
    search_distance, distance_unit, aggregate_links, sum_fields)