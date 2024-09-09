import arcpy
arcpy.CreateSpatialType_management(
    "/ragsrh/users/connections/connection_to_sp_pg.sde", "$Upass", "sdetbsp", 
    "/st_geometry/libst_shapelib.so")