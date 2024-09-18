import arcpy
arcpy.env.workspace = "C:/data/airport.gdb"
arcpy.management.CalculateFields(
    "parcels", "ARCADE", 
    [["max_value", "Max($feature.field1, $feature.field2)"], 
     ["min_value", "Min($feature.field1, $feature.field2)"]])