import arcpy

# Import toolbox with custom model inside
arcpy.ImportToolbox("c:/gisworkflows/ParcelTools.tbx")

# Run the tool and assign to a result variable
parcelUpdate = arcpy.ParcelUpdater_ParcelTools("c:/data/parcels.gdb/ward3", "UPDATE")

arcpy.management.PackageResult(parcelUpdate.resultID, "c:/gpks/parcelgpk.gpkx", 
                               "PRESERVE", "CONVERT_ARCSDE", "#", "ALL", 
                               "ALL", "DESKTOP", "#", "Summary text", "Tag1")