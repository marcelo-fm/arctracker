import arcpy
arcpy.management.SetRelationshipClassSplitPolicy("C:\\MyProject\\sdeConn.sde\\progdb.user1.ParcelsToBuildings", 
                                                 "DUPLICATE_RELATED_OBJECTS")