import arcpy
arcpy.parcel.UpgradeArcMapParcelFabric(
    "C:/Data/Database.gdb/Parcels/CountyFabric", 
    "C:/Data/Database.gdb/ParcelsPro", "UpgradedFabric", 'DELETE_IDENTICAL_LINES')