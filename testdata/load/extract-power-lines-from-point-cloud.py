arcpy.env.workspace = "c:/data"
arcpy.ddd.ExtractPowerLinesFromPointCloud("Electrical_Assets.lasd", 14, 
                                          "Power_Lines.shp", "80 Centimeters")