import arcpy
arcpy.tn.CreateTraceNetwork(r"C:\MyProject\MyNetworkGdb.gdb\Hydro", "HydroNetwork", "PourPoints","HydroLines COMPLEX_EDGE;BlackLines SIMPLE_EDGE")