import arcpy
arcpy.ba.GenerateTradeAreaRings("sales_locations.shp",r"sales_locations_GenerateTrad.shp", [1, 3, 5],"MILES", "ID", "KEEP_OVERLAP", Values, None)