import arcpy
arcpy.SetNetworkAttribute_tn("Trace Network", "Friction Factor", 
                             "BlackLines", "frictionvalue")