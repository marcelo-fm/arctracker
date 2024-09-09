import arcpy
arcpy.env.workspace = 'd:\\data'
arcpy.ddd.SunShadowFrequency('Buildings.shp', 'DEM.tif', 'June_Shade.tif',
                             '4 Feet', '6/1/2018 10:00 AM', '6/30/2018 4:00 PM',
                             '15 Minutes', 'Pacific Standard Time', 'NO_DST')