import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddForceDirectedLayout_nd(input_Network, "MyTemplate1", "ACTIVE", 
                                "PRESERVE_CONTAINERS", 20, 1, "LOW", "25", 
                                "CURVED_EDGES")