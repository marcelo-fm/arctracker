import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "SameAsBasicTemplate"
arcpy.nd.AddDiagramTemplate(input_Network, input_DiagramTemplate)
arcpy.nd.AlterDiagramTemplate(input_Network, input_DiagramTemplate, 
                              input_DiagramTemplate, "NOT_DEFAULT_TEMPLATE", 
                              "DO_NOT_REMOVE_RULES_AND_LAYOUTS",
                              "KEEP_VERTICES", "0.3 Meters")
arcpy.nd.AddConnectivityAssociationsRule(input_Network, 
                                         input_DiagramTemplate, "ACTIVE")
arcpy.nd.AddStructuralAttachmentsRule(input_Network, 
                                      input_DiagramTemplate, "ACTIVE")