import arcpy
arcpy.ApplyGeoPositionsLayout_nd('Temporary Diagram', 
                                 "RESTORE_EDGES_GEO_POSITIONS", 
                                 "RUN_SYNCHRONOUSLY")