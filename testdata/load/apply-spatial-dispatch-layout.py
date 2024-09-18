import arcpy
arcpy.ApplySpatialDispatchLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", 
                                    5, 2, "RUN_SYNCHRONOUSLY")