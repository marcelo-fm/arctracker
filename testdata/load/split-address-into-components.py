import arcpy

atlanta_addresses = r"C:\AtlantaAddresses.csv"
arcpy.geocoding.SplitAddressIntoComponents("USA", atlanta_addresses, "Address", 
                                           r"C:\MySplitAddresses.csv", 
                                           "ExceptionsFile.csv")