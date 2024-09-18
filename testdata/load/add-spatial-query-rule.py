import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DistributionLine = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionLine"
input_StructureBoundary = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricStructureBoundary"

input_DiagramTemplate = "MyTemplate1"

arcpy.nd.AddSpatialQueryRule(input_Network, input_DiagramTemplate, 
                             'ACTIVE', input_DistributionLine, 'INTERSECT',
                             input_StructureBoundary, None, 'ASSETGROUP=6', 
                             'ASSETGROUP=3')