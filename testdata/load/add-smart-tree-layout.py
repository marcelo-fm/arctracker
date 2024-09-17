import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddSmartTreeLayout_nd(input_Network, input_DiagramTemplate, 
                            "ACTIVE", "PRESERVE_CONTAINERS", 
                            "FROM_LEFT_TO_RIGHT", "PROPORTIONAL_UNIT", "", 8, 
                            "", 5, "", 5, "", 15, "", 25, "CURVED_EDGES")