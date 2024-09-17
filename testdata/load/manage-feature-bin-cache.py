import arcpy
arcpy.management.ManageFeatureBinCache("lod_gdb.elec.Earthquakes", "SQUARE", 
                                       "STATE", "depth_km MAX")