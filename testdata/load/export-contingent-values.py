import arcpy
arcpy.ExportContingentValues_management("C:\\MyProject\\myConn.sde\\pro.USER1.Animals",
                                        "C:\\MyProject\\MyFieldGroups.csv",
                                        "C:\\MyProject\\MyContingentValues.csv")