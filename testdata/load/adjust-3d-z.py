arcpy.env.workspace = "C:/data"
arcpy.Adjust3DZ_management("subsurface_pts.shp", "REVERSE", 0, "METERS", "FEET")