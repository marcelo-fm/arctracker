import arcpy
arcpy.env.workspace = r"C:\data\US_Streams.gdb"
arcpy.management.GenerateRectanglesAlongLines("StreamReach", "riparian_zones", 
                                              "250 Meters", "180 Meters", "UR")