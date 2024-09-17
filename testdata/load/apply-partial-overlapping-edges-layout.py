import arcpy
arcpy.ApplyPartialOverlappingEdgesLayout_nd("Temporary Diagram", "15 Feet", 
                                            "25 Feet", "DO_NOT_OPTIMIZE_EDGES", 
                                            "RUN_SYNCHRONOUSLY")