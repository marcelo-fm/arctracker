import arcpy
arcpy.ba.AssignCustomersByDistance("SF_Custs", "SF_Stores", "STORE_ID",
                                   r"C:\ArcGIS\Projects\MyProject.gdb\SF_Custs_AssignCustomersByDistance",
                                   "STORE_ID_1", "Driving Time", "MINUTES",
                                   "TOWARD_STORES", None,
                                   "TIME_ZONE_AT_LOCATION")