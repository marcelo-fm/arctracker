import arcpy
arcpy.nd.ApplyRotateTreeLayout("Temporary Diagram", "PRESERVE_CONTAINERS", 90, 
                               "RUN_SYNCHRONOUSLY", "ROTATE")