import arcpy
arcpy.env.workspace = "c:/gis_data"
arcpy.management.CreateSceneLayerPackage(
    "Milan.lyrx", "Milan.slpk", arcpy.SpatialReference(4326), 
    ["ITRF_2000_To_WGS_1984 + WGS_1984_To_WGS_1984_EGM2008_2.5x2.5_Height"],
    ["INTENSITY", "RGB", "CLASS_CODE", "FLAGS", "RETURNS"], 0, 0.1, 0.1, None, 
    "1.X")