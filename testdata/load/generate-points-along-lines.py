# Description: Convert point features to line features

import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data/base.gdb'

# Set local variables
in_features = 'rivers'
out_fc_1 = 'distance_intervals'
out_fc_2 = 'percentage_intervals'

# Run GeneratePointsAlongLines by distance
arcpy.management.GeneratePointsAlongLines(in_features, out_fc_1, 'DISTANCE',
                                          Distance='500 meters')

# Run GeneratePointsAlongLines by percentage
arcpy.management.GeneratePointsAlongLines(in_features, out_fc_2, 'PERCENTAGE',
                                          Percentage=10,
                                          Include_End_Points='END_POINTS')