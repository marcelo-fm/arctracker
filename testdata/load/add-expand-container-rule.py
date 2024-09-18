import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_DoNotExpandSourceClass = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricDistributionAssembly"

arcpy.nd.AddExpandContainerRule(input_Network, input_DiagramTemplate, 
                                'ACTIVE', 'KEEP_VISIBLE', 'BOTH', 
                                'EXCLUDE_SOURCE_CLASSES', 
                                input_DoNotExpandSourceClass)