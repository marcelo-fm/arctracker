import arcpy
input_Network = 'D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric'
input_NetworkCategory = 'Subnetwork Controller'
input_DiagramTemplate = 'MyTemplate1'

arcpy.nd.AddDiagramFeatureCapabilityByAttributeRule(
    input_Network, input_DiagramTemplate, 'ACTIVE', 'INCLUDE_CATEGORIES',
    input_NetworkCategory, 'PREVENT_TO_COLLAPSE_CONTAINER')