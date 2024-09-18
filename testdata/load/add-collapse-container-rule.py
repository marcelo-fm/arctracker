import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_DoNotCollapseSourceClass = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.StructureJunction"

arcpy.nd.AddCollapseContainerRule(input_Network, input_DiagramTemplate, 
                                  'ACTIVE', 'BOTH', 'EXCLUDE_SOURCE_CLASSES', 
                                  input_DoNotCollapseSourceClass, None,
                                  'AGGREGATE_RECONNECTED_EDGES')