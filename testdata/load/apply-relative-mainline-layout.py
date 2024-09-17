import arcpy
arcpy.nd.ApplyRelativeMainlineLayout("Temporary Diagram", "LineTrack", 
                                     "FROM_LEFT_RIGHT", 2, 45, "RUN_SYNCHRONOUSLY")