import arcpy
arcpy.SetFlowDirection_tn("C:\\MyProject\\NHD.gdb\\Hydro\\HydroNetwork_v1", 
                          "HydroLines", "WITH_DIGITIZED_DIRECTION")