import arcpy

input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate2"
input_JunctionClassToReduce1 = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionJunction"
input_Alias1 = "Asset type"
input_Alias2 = "Phases"

arcpy.nd.AddReduceJunctionRule(
    input_Network, input_DiagramTemplate, "ACTIVE", 
    'INCLUDE_SOURCE_CLASSES', input_JunctionClassToReduce1, 
    "MAX_2_CONNECTED_JUNCTIONS", "KEEP_UNCONNECTED_JCT", "KEEP_JCT_TO_1JCT",
    "REDUCE_JCT_TO_2JCTS", input_Alias1 + ";" + input_Alias2)