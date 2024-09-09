import arcpy
arcpy.env.workspace = "C:/data/cartography.gdb/transportation"
arcpy.cartography.CollapseRoadDetail("roads.lyr", "250 Feet", "roads_collapse_250")