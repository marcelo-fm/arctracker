import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.nd.AddCompressionLayout(input_Network, input_DiagramTemplate, "ACTIVE", 
                              "PRESERVE_CONTAINERS", "20 Feet", "OUTER")