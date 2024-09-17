import arcpy
arcpy.env.workspace = "C:/Dataspace/WhereMyCatalogLayerIs.gdb"
arcpy.management.AddItemsToCatalogDataset(
    "MyCatalogDataset", ["AllMyFeatures.gdb", "AllMyRasters.gdb"], 
    ["FEATURE_CLASS", "RASTER_DATASET"], "INCLUDE_SUBFOLDERS", "ENVELOPE")