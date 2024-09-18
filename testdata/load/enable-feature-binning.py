import arcpy

bin_coord_sys = arcpy.SpatialReference('GCS_WGS_1984')
arcpy.management.EnableFeatureBinning(
    "lod_gdb.elec.Earthquakes", 
    "SQUARE", 
    bin_coord_sys,
    "depth_km MAX", 
    "STATIC_CACHE")