import arcpy
input_Network = 'D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric'
input_DiagramTemplate = 'MyTemplate1'
input_Category = 'LinearContainer'

arcpy.nd.AddRemoveFeatureRule(
    input_Network, input_DiagramTemplate, 'ACTIVE', 'EDGES',
    'INCLUDE_SOURCE_CLASSES', input_Category)