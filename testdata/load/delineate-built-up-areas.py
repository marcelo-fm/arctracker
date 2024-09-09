import arcpy
arcpy.env.workspace = "C:/data"
env.referenceScale = "50000"
arcpy.DelineateBuiltUpAreas_cartography("bldg_pnt;bldg_poly",
                                        "inBUA",
                                        "RoadNetwork",
                                        "100 Meters",
                                        "125 Meters",
                                        "BUApolypoint", 
                                        6)