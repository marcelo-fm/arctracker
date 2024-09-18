import arcpy

arcpy.parcel.ImportParcelFabricPoints(
    "C:/Parcels/Database.gdb/UpdatePoints",
    "C:/Parcels/Database.gdb/County/CountyFabric", 'PROXIMITY', '0.1 Feet', 
    'ALL', 'Record001', None, "C:/Parcels/Database.gdb/ConflictsTable", 'UPDATE_AND_CREATE')