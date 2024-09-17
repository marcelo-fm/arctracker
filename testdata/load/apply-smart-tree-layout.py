import arcpy
arcpy.ApplySmartTreeLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", 
                              "FROM_LEFT_TO_RIGHT", "PROPORTIONAL_UNIT", 
                              "", 8, "", 5, "", 5, "", 15, "", 70, 
                              "REGULAR_EDGES", "RUN_SYNCHRONOUSLY")