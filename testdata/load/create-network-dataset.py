import arcpy
arcpy.CheckOutExtension("network")

arcpy.na.CreateNetworkDataset(r"C:\Data\Network.gdb\Transportation", 
                              "Streets_ND", ["Streets", "Turns"], 
                              "ELEVATION_FIELDS")