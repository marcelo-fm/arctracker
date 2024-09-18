import arcpy
arcpy.un.AddRule("Electric Network", "STRUCTURAL_ATTACHMENT", 
                 "StructureJunction", "Pole", "Wood", 
                 "ElectricDistributionDevice", "Switch", 
                 "Overhead Low Voltage Single Phase Disconnect")