import arcpy
arcpy.GeodeticDensify_management(r"C:\data.gdb\flight_lines", 
                                 r"C:\data.gdb\flight_lines_geodesic", 
                                 "GEODESIC")