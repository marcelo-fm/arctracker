import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_EdgeLineClassToReduce = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionLine"

arcpy.AddReduceEdgeByAttributeRule_nd(input_Network, input_DiagramTemplate, 
                                      'ACTIVE', input_EdgeLineClassToReduce, 
                                      "ASSETGROUP = 1", '', 
                                      'AGGREGATE_RECONNECTED_EDGES')