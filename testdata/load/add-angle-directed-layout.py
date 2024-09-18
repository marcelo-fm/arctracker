import arcpy
input_Network = 'D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric'
input_DiagramTemplate = 'MyTemplate1'

arcpy.AddAngleDirectedLayout_nd(input_Network, input_DiagramTemplate, 
                                'ACTIVE', 'PRESERVE_CONTAINERS', 20, 
                                'EIGHT_DIRECTIONS')