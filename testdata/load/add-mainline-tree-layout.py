import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddMainlineTreeLayout_nd(input_Network, input_DiagramTemplate, 
                               "ACTIVE", "PRESERVE_CONTAINERS", 
                               "FROM_LEFT_TO_RIGHT", "BOTH_SIDES", 
                               "ABSOLUTE_UNIT", "100 Feet", "", "100 Feet", "", 
                               "200 Feet", "", "", 30, "ORTHOGONAL_EDGES", 
                               "10 Feet")