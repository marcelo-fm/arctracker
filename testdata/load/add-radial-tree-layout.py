import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddRadialTreeLayout_nd(input_Network, input_DiagramTemplate, "ACTIVE", 
                             "PRESERVE_CONTAINERS", "ABSOLUTE_UNIT", 5, "", 15, "", 1)