import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.nd.AddTraceRule(input_Network, input_DiagramTemplate, "ACTIVE", 
                      "SUBNETWORK", "ElectricDistribution", "Medium Voltage", 
                      "Low Voltage Mesh")