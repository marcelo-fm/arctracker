import arcpy
arcpy.management.GeneratePointCloud('c:/data/BD.gdb/SpringMD', 'ETM',
                                    'c:/data/output', 'SpringLAS', '10')