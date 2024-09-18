import arcpy
arcpy.env.workspace = "C:\data\data.gdb"
arcpy.edit.SimplifyByStraightLinesAndCircularArcs("myDensifiedPolygons;myDensifiedLines", 
                                                  "0.4 Meters", 
                                                  anchor_points="myAnchorPoints")