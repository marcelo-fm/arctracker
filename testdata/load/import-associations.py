import arcpy
arcpy.un.ImportAssociations("GridNetwork", "STRUCTURAL_ATTACHMENT", 
                            "C:\\Temp\\StructuralAttachment.csv")