import arcpy
arcpy.parcel.AnalyzeParcelsByLeastSquaresAdjustment('c:/Parcels/Database.gdb/CountyParcels/CountyFabric', 
                                                    'CONSISTENCY_CHECK', 0.05)