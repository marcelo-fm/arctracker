import arcpy
arcpy.env.workspace = "C:/data/localhost.sde"
arcpy.management.MakeAggregationQueryLayer(
    "weather_stations", "station_id", "observed_rainfall", "station_id", 
    "Total_Rainfall", [["SUM", "rainfall_inch"], ["MIN", "rainfall_inch"]], 
    "RANGE TimeVar # collection_date DATE 1/1/2020 12/1/2020 NONE # NONE")