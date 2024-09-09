import arcpy

# Access data locally.
arcpy.env.baDataSource = "LOCAL;;USA_ESRI_2020"
arcpy.ba.FindNearbyLocations("FindNearby.gdb/stores", "STORE_ID", "FindNearby.gdb/coffee", "FindNearby.gdb/Nearby_coffee_competitors", "STRAIGHT_LINE_DISTANCE", "MILES", None, "10", None, "DO_NOT_CREATE_REPORT", None, "#", None, None, "TOWARD_STORES", None, "TIME_ZONE_AT_LOCATION", None")