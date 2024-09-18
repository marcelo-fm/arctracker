import arcpy
arcpy.ApplyForceDirectedLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", 
                                  20, 1, "LOW", 25, "CURVED_EDGES", 
                                  "RUN_SYNCHRONOUSLY")