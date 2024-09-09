import os
import arcpy
arcpy.env.overwriteOutput = True

# Create hexagons
out_gdb = arcpy.env.scratchGDB
hex_fc = os.path.join(out_gdb, 'out_fc_hex_2')

arcpy.management.GenerateTessellation(
    hex_fc, '-10823285.769168 4836611.80759869 -10781728.9441187 4856999.87422328', 
    'HEXAGON', '17269676,2624 Unknown', arcpy.SpatialReference(3857))

# Create 2 random points in each hexagon
count_pts = 2
pts_fc = arcpy.management.CreateRandomPoints(
    out_gdb, 'out_fc_crp_2', constraining_feature_class=hex_fc, 
    number_of_points_or_field=count_pts)[0]

# Join the point attributes based on points within the hexagons
result = arcpy.management.AddSpatialJoin(
    hex_fc, pts_fc, None, None, 'CID', 'COMPLETELY_CONTAINS')