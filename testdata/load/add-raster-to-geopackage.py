import arcpy
arcpy.conversion.AddRasterToGeoPackage("c:/data/san_diego.png", "c:/data/san_diego.gpkg", 
                                       "SanDiego", "TILED")