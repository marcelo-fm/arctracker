import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddPartialOverlappingEdgesLayout_nd(input_Network, 
                                          input_DiagramTemplate, "ACTIVE", 
                                          "15 Feet", "25 Feet", 
                                          "DO_NOT_OPTIMIZE_EDGES")