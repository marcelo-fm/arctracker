import arcpy
arcpy.nd.ApplyLinearDispatchLayout("Temporary Diagram", "ITERATIVE_DISTANCE", 
                                   "ABSOLUTE_UNIT", "15 Feet", "", "2 Feet", 
                                   "", 10, "PRESERVE_PATH", "DO_NOT_MOVE_LEAVES", 
                                   "DO_NOT_EXPAND_LEAVES", "2 Feet", 2, 
                                   "RUN_SYNCHRONOUSLY")