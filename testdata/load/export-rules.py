import arcpy
arcpy.ExportRules_un("GridNetwork", "STRUCTURAL_ATTACHMENT", 
                     r"C:\Temp\StructureAssociationRules.csv")