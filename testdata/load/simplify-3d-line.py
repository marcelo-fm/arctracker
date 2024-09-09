import arcpy
arcpy.env.workspace = 'C:/data'
arcpy.ddd.Simplify3DLine('rivers.shp', 'simplified_rivers.shp', '2 Meters')