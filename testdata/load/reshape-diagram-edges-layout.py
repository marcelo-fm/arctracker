import arcpy
arcpy.nd.ReshapeDiagramEdgesLayout("Temporary Diagram", "PRESERVE_CONTAINERS", 
                                   "REDUCE_VERTICES_BY_ANGLE", angle_threshold=160)