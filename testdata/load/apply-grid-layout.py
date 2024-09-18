import arcpy
arcpy.ApplyGridLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", "2 Feet", 
                         "5 Feet", "RUN_SYNCHRONOUSLY")