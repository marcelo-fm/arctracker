import arcpy
arcpy.management.SetFeatureClassSplitModel("C:\\MyProject\\sdeConn.sde\\progdb.user1.Parcels", 
                                           "DELETE_INSERT_INSERT")