import arcpy
arcpy.management.TrimArchiveHistory("C:\\MyProject\\myGdb.sde\\mydatabase.user1.Parcels", 
                                    "DELETE", "2020/03/10 10:28:56 AM")