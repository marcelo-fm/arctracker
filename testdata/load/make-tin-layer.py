import arcpy
arcpy.env.workspace = 'C:/gis_data/input'
arcpy.management.MakeTinLayer('dtm', 'Elevation Layer')