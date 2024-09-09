import arcpy
arcpy.management.AddRelate("Parcel", "ParcelID", "owner_table", "ParcelID", 
                           "Owner2Parcel")