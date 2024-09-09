import arcpy
from arcpy import env

env.workspace = 'C:/data'
arcpy.Intersect3DLineWithSurface_3d('lines.shp', 'dtm_tin; elev.tif',
                                  'intersect_lines.shp', 'intersect_pts.shp')