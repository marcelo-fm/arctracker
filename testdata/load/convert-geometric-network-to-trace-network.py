import arcpy
arcpy.tn.ConvertGeometricNetworkToTraceNetwork("C:\\MyTNProject\\NHD.gdb\Hydro\HydroGN",
                                               "HydroTN")