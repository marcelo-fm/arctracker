import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"
input_ClassToRemove = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.ElectricTransmissionLine"

arcpy.nd.AddRemoveFeatureByAttributeRule(input_Network, input_DiagramTemplate,
                                         "ACTIVE", input_ClassToRemove, "PLACEMENT=1")