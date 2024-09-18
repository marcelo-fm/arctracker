import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate2"
input_JunctionClassToReduce = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionDevice"
input_Alias1 = "Asset type"
input_Alias2 = "Phases"

arcpy.nd.AddReduceJunctionByAttributeRule(input_Network, input_DiagramTemplate, 
                                          "ACTIVE", input_JunctionClassToReduce, 
                                          "ASSETTYPE <> 11 And ASSETTYPE <> 8", 
                                          "MAX_2_CONNECTED_JUNCTIONS", 
                                          "KEEP_UNCONNECTED_JCT", "KEEP_JCT_TO_1JCT",
                                          "REDUCE_JCT_TO_2JCTS", 
                                          input_Alias1 + ";" + input_Alias2)