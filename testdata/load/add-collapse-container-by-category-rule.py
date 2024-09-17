import arcpy
input_Network = 'D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric'
input_DiagramTemplate = 'MyTemplate1'
input_Category = 'Duct Bank'

arcpy.nd.AddCollapseContainerByCategoryRule(
    input_Network, input_DiagramTemplate, 'ACTIVE', 'EDGES',
    'INCLUDE_CATEGORIES', input_Category, 'AGGREGATE_RECONNECTED_EDGES')