import arcpy

arcpy.ApplyMainlineTreeLayout_nd("Temporary Diagram", "PRESERVE_CONTAINERS", 
                                 "FROM_LEFT_TO_RIGHT", "BOTH_SIDES", 
                                 "ABSOLUTE_UNIT", "100 Feet", "" , "100 Feet", 
                                 "", "200 Feet", "", "", 30, "ORTHOGONAL_EDGES", 
                                 "RUN_SYNCHRONOUSLY", "10 Feet", "")