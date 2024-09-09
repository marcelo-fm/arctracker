import arcpy
arcpy.env.workspace = r"C:/GIS_Data"
arcpy.ddd.ExtractObjectsFromPointCloud("Terrestrial_Scan.lasd", [(4, 5), (5, 5)],
                                       "60 Centimeters", "Trees.shp", 
                                       "CONCAVE_HULL_2D", 50)