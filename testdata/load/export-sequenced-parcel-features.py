import arcpy
arcpy.parcel.ExportSequencedParcelFeatures(
    'C:/Parcels/Database.gdb/Parcels/CountyFabric/Lot',
    'C:/Parcels/Database.gdb/Layout', 'NE', '#', '#',
    'SEQUENCE_SEPARATELY')