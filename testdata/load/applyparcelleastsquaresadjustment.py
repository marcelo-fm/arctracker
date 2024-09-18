import arcpy
arcpy.parcel.ApplyParcelLeastSquaresAdjustment('c:/Parcels/Database.gdb/CountyParcels/CountyFabric',
                                               0.05, 'NO_UPDATE_ATTRIBUTES')