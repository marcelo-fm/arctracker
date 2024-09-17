import arcpy
arcpy.parcel.BuildParcelFabric("C:/Data/Database.gdb/Parcels/CountyFabric", 
                               "MAXOF")