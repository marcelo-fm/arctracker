import arcpy
arcpy.env.workspace = "C:\GIS_Data"
arcpy.ddd.PointCloudToRaster("GT_Mountains.slpk", "10 Meters", "GT_surface.tif",
                             "MAXIMUM", "LINEAR", "0.3048")