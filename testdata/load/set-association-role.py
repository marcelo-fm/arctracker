import arcpy
arcpy.un.SetAssociationRole("Utility Network", "ElectricDistribution", 
                            "ElectricDistributionAssembly", "Transformer Bank", 
                            "Transformer", "CONTAINER", "RESTRICTED", 10)