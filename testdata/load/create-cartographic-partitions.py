import arcpy
arcpy.env.workspace = "C:/data/cartography.gdb/transportation"
arcpy.CreateCartographicPartitions_cartography("roads.lyr", "partitions", 50000, "FEATURES")