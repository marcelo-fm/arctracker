import arcpy
arcpy.ApplyAngleDirectedLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", 
                                  20, "EIGHT_DIRECTIONS", "RUN_SYNCHRONOUSLY")