import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_DeviceClass = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatase.MAP.ElectricDistributionDevice"

arcpy.AddSetRootJunctionByAttributeRule_nd(input_Network, input_DiagramTemplate, 
                                           "ACTIVE", input_DeviceClass, 
                                           "ASSETTYPE = 5 And ENABLED = 1")