import arcpy
arcpy.env.workspace = "C:/data"
arcpy.parcel.CopyParcels('CountyFabric', "C:/Parcels/Database.gdb")