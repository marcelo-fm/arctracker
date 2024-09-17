import arcpy

input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "Template1"
input_StructureJunction = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.StructureJunction"
input_DistributionAssembly = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionAssembly"
input_DistributionDevice = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionDevice"
input_MiscJunction = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionJunction"
input_SystemJunctions = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.UN_112_SystemJunctions"

arcpy.AddDiagramTemplate_nd(input_Network, input_DiagramTemplate)

arcpy.AddTraceRule_nd(input_Network, input_DiagramTemplate, "ACTIVE", 
                      "SUBNETWORK", "ElectricDistribution", "Medium Voltage", 
                      "Low Voltage Mesh")

arcpy.AddRemoveFeatureRule_nd(input_Network, input_DiagramTemplate, 
                              'ACTIVE', 'INCLUDE_SOURCE_CLASSES', 
                              input_StructureJunction + ";" + input_DistributionAssembly)

arcpy.AddStartIterationRule_nd(input_Network, input_DiagramTemplate, 
                               'ACTIVE')

arcpy.AddReduceJunctionRule_nd(input_Network, input_DiagramTemplate, 
                               'ACTIVE', 'INCLUDE_SOURCE_CLASSES', 
                               input_SystemJunctions + ";" + input_MiscJunction, 
                               "MAX_2_CONNECTED_JUNCTIONS", 
                               "REDUCE_UNCONNECTED_JCT", 
                               "REDUCE_JCT_TO_1JCT", "REDUCE_JCT_TO_2JCTS")

arcpy.AddReduceJunctionByAttributesRule_nd(input_Network, 
                                           input_DiagramTemplate, 'ACTIVE', "", 
                                           input_DistributionDevice, 
                                           "ASSETGROUP NOT IN (4, 15)", 
                                           "MAX_2_CONNECTED_JUNCTIONS", 
                                           "REDUCE_UNCONNECTED_JCT", 
                                           "REDUCE_JCT_TO_1JCT", 
                                           "REDUCE_JCT_TO_2JCTS")

arcpy.AddReduceJunctionRule_nd(input_Network, input_DiagramTemplate, 
                               'ACTIVE', 'INCLUDE_SOURCE_CLASSES', 
                               input_SystemJunctions + ";" + input_MiscJunction, 
                               "MIN_3_CONNECTED_JUNCTIONS")

arcpy.AddStopIterationRule_nd(input_Network, input_DiagramTemplate, 
                              'ACTIVE')