import arcpy
arcpy.ApplyMainRingLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", 
                             "ELLIPSE", "PROPORTIONAL_UNIT", "", 50, "", 20, 
                             "SMART_TREE", "", 2, "", 2, 25, "CURVED_EDGES", 
                             "RUN_SYNCHRONOUSLY")