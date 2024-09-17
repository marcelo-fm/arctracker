import arcpy
arcpy.un.ExportSubnetwork("Utility Network", "ElectricDistribution", 
                          "Medium Voltage", "RMT002", "ACKNOWLEDGE", 
                          "C:\\Temp\\RMT002clean.json", None, None, 
                          "INCLUDE_BARRIERS", "BOTH_JUNCTIONS_AND_EDGES", 
                          None, "EXCLUDE_GEOMETRY", None, None, None, 
                          "INCLUDE_DOMAIN_DESCRIPTIONS")