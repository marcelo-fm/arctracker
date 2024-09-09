import arcpy
arcpy.env.baDataSource = "USA_ESRI_<year>"
arcpy.ba.EnrichLayer("TradeArea1", "TradeArea1_Enrich", r" C:\Users\<USER ID>\Documents\ArcGIS\Projects\My_Project\BayArea_ProprietaryData.sdcx/sales_s01_sales", None, 1, None)