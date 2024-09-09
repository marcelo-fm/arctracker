import arcpy
arcpy.ba.CalculateMarketPenetration("UC_West", r"MyProject.gdb\UC_West", "id", "TOTHH_CY", "Cust_Points", "name", "Sales", "DO_NOT_CREATE_REPORT", None, None, None, None, None)