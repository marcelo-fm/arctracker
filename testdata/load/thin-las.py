arcpy.env.workspace = 'C:/data'
arcpy.ddd.ThinLas('photogrammetric_cloud.lasd', 'thinned', '3D', 
                  '20 Centimeters', '15 Centimeters', 'Z_AVERAGE', 
                  excluded_flags='WITHHELD', rearrange_points='REARRANGE_POINTS')