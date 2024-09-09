import arcpy
arcpy.env.baDataSource = "ONLINE;US;"
arcpy.ba.SummaryReports("TradeArea50", "Age 50+ Profile", r"C:\Temp", "INDIVIDUAL_FEATURES", "CREATE_REPORT_PER_TEMPLATE", "PDF", "ID", None, None, "STORE_LAT", "STORE_LONG", "RING", "AREA_DESC", "Age 50 Plus Store Trade Area", "Prepared By Business Analyst Pro", "CREATE_REPORT_PER_FEATURE")