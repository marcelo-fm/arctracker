import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_StructureJunctionToExpand = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.StructureJunction"

arcpy.nd.AddExpandContainerByAttributeRule(input_Network, input_DiagramTemplate, 
                                           "ACTIVE", "KEEP_VISIBLE", 
                                           input_StructureJunctionToExpand, 
                                           "ASSETTYPE <> 8")