import arcpy
arcpy.env.workspace = 'C:/data/city_models.gdb'
arcpy.management.Add3DFormats('Downtown_Buildings', 'MULTIPATCH_WITH_MATERIALS', 
                              ['FMT3D_DAE', 'FMT3D_OBJ'])