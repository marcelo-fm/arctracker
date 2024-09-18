import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_DoNotRemoveThisClass = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricTransmissionLine"

arcpy.nd.AddRemoveFeatureRule(input_Network, input_DiagramTemplate, 
                              'ACTIVE', 'EDGES', 'EXCLUDE_SOURCE_CLASSES', 
                              input_DoNotRemoveThisClass)