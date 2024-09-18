import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"

arcpy.nd.AlterDiagramTemplate(input_Network, "ExpandContainers", 
                              "ExpandContainers", "NOT_DEFAULT_TEMPLATE", 
                              "DO_NOT_REMOVE_RULES_AND_LAYOUTS",
                              "KEEP_VERTICES", "0.3 Meters", 
                              "ENABLE_DIAGRAM_STORAGE", 
                              "DISABLE_DIAGRAM_EXTENSION",
                              None, 
                              "DO_NOT_REMOVE_LAYER_DEFINITIONS")