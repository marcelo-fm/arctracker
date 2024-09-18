import arcpy
arcpy.Trace_tn(r"C:\MyProject\NHD.gdb\Hydro\HydroNetwork", 
               "DOWNSTREAM", r"C:\MyProject\NHD.gdb\TN_Temp_Starting_Points")