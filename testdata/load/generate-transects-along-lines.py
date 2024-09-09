# Description: Add sampling perpendicular transect lines along a river

import arcpy

# Set environment settings
arcpy.env.workspace = 'C:/data/base.gdb'

# Set local variables
in_features = 'rivers'
out_fc_1 = 'river_samples_transects'

# Execute GeneratePointsAlongLines by distance
arcpy.GenerateTransectsAlongLines_management(in_features, out_fc_1, '100 Meters',
                                             '100 meters', 'END_POINTS')