import arcpy
arcpy.ApplyRadialTreeLayout_nd("Temporary diagram", "PRESERVE_CONTAINERS", 
                               "ABSOLUTE_UNIT", 5, "", 15, "", 1, 
                               "RUN_SYNCHRONOUSLY")