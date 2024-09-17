import arcpy
arcpy.env.workspace = "C:/data/city_models.gdb"
arcpy.management.Remove3DFormats('Downtown_Buildings', 
                                 'MULTIPATCH_WITHOUT_MATERIALS', 
                                 ['FMT3D_DAE', 'FMT3D_OBJ'])