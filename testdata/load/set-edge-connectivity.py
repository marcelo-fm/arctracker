import arcpy
arcpy.SetEdgeConnectivity_un("Utility Network", "ElectricDistribution", 
                             "ElectricDistributionLine", "Connector", 
                             "Connector", "EndVertex")