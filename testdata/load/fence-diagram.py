arcpy.env.workspace = 'c:/data'
arcpy.ddd.FenceDiagram('fence_profile.shp', 
                       ['alluvium.tif', 'white_limestone.tif', 'yellow_limestone.tif'], 
                       'fence_diagram.shp', sample_distance='5 Meters')