import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_StructureDeviceToCollapse = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.StructureJunction"

arcpy.nd.AddCollapseContainerByAttributeRule(input_Network, input_DiagramTemplate, 
                                             "ACTIVE", input_StructureDeviceToCollapse, 
                                             "ASSETGROUP <> 8", '', 'AGGREGATE_RECONNECTED_EDGES')