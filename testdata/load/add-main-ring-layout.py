import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddMainRingLayout_nd(input_Network, "MyTemplate1", "ACTIVE", 
                           "PRESERVE_CONTAINERS", "ELLIPSE", 
                           "PROPORTIONAL_UNIT", "", 50, "", 20, "SMART_TREE", 
                           "", 2, "", 2, 30, "CURVED_EDGES")