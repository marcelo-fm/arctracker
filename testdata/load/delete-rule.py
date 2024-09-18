import arcpy
arcpy.un.DeleteRule("Electric Network", "STRUCTURAL_ATTACHMENT", 
                    "126: From[StructureJunction.Pole] To[ElectricDistributionDevice.ServicePoint]")