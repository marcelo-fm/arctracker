import arcpy
arcpy.nd.ApplyCompressionLayout("Temporary Diagram", "PRESERVE_CONTAINERS", 
                                "20 Feet", "OUTER", "RUN_SYNCHRONOUSLY")