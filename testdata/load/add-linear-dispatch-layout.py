import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddLinearDispatchLayout_nd(input_Network, input_DiagramTemplate, 
                                 "ACTIVE", "ITERATIVE_DISTANCE", "ABSOLUTE_UNIT", 
                                 "15 Feet", "", "2 Feet", "", 10, "PRESERVE_PATH", 
                                 "DO_NOT_MOVE_LEAVES", "DO_NOT_EXPAND_LEAVES", 
                                 "2 Feet", 2)