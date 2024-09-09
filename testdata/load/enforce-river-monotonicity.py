import arcpy
arcpy.env.workspace = "C:\GIS_Data"
arcpy.ddd.EnforceRiverMonotonicity("River_Polygons_3D.shp", "River_Flow_Directions.shp",
                                   "River_Breaklines_3D.shp", "10 Meters", "5 Meters")