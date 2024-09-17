import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DistributionDevice = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionDevice"

input_DiagramTemplate = "MyTemplate1"

arcpy.nd.AddDiagramFeatureCapabilityByAttributeRule(
    input_Network, input_DiagramTemplate, 'ACTIVE', 
    input_DistributionDevice, 'ASSETGROUP=14', "PREVENT_TO_COLLAPSE_CONTAINER")