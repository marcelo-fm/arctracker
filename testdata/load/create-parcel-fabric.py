import arcpy
arcpy.parcel.CreateParcelFabric("C:/Data/Parcels/Database.gdb/CountyParcels", 
                                "County Fabric")