import arcpy
arcpy.env.workspace = 'C:/data'
arcpy.ddd.Intersect3DLines(['floor_centerlines.shp', 'stairs.shp'], '2 Meters', 
                           'ONLY_FID', 'intersection_pts.shp')