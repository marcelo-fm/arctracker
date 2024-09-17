import arcpy
arcpy.parcel.CreateParcelRecords(r'c:\Data\Database.gdb\Parcels\Lot', '', 
                                 'Left($feature.Name,4)', 'EXPRESSION')