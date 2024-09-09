import arcpy
arcpy.env.baDataSource = "ONLINE;US;"
arcpy.ba.DesireLines("grocery stores", "grocery customers", r"C:\Temp\Output.gdb\grocery stores_DesireLines", "USER_STORE_ID", "USER_STORE_ID", "STRAIGHT_LINE_DISTANCE", "MILES", None, "TOWARD_STORES", None, "TIME_ZONE_AT_LOCATION", "CREATE_REPORT", '', r"C:\Temp\Output.gdb\DesireLines", "PDF")