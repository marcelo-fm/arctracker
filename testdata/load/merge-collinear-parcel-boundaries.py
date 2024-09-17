import arcpy
arcpy.parcel.MergeCollinearParcelBoundaries("C:/Data/Database.gdb/Parcels/CountyFabric/Tax_Lines", '0.5 Feet')