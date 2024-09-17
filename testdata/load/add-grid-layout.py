import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddGridLayout_nd(input_Network, input_DiagramTemplate, "ACTIVE", 
                       "PRESERVE_CONTAINERS", "2 Meter", "5 Meter")