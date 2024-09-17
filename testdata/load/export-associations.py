import arcpy
arcpy.ExportUtilityNetworkAssociations_un("GridNetwork", "STRUCTURAL_ATTACHMENT", 
                                          r"C:\Temp\StructureAssociations.csv")