import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddReshapeDiagramEdgesLayout_nd(input_Network, input_DiagramTemplate, 
                                      "ACTIVE", "PRESERVE_CONTAINERS", 
                                      "SQUARE_EDGES", "PRESERVE_PATH", "5 Feet", 
                                      "8.66 Feet")