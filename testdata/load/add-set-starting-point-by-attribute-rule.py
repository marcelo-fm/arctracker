import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_Device = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionDevice"

arcpy.nd.AddSetStartingPointByAttributeRule(input_Network, input_DiagramTemplate, 
                                             "ACTIVE", input_Device, 
                                             "ASSETGROUP <> 4", "3")