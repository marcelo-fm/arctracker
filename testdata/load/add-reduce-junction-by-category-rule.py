import arcpy

input_Network = 'D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric'
input_DiagramTemplate = 'MyTemplate1'
input_Category1 = 'Subnetwork Controller'
input_Category2 = 'Switch'

arcpy.nd.AddReduceJunctionRule(
    input_Network, input_DiagramTemplate, 'ACTIVE', 'EXCLUDE_CATEGORIES',
    [input_Category1, input_Category2], 'MAX_2_CONNECTED_JUNCTIONS',
    'REDUCE_UNCONNECTED_JCT', 'REDUCED_JCT_TO_1JCT', 'REDUCE_JCT_TO_2JCTS')