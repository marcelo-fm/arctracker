import arcpy
input_Network = "D:/MyProjectLocation/MyDatabaseConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DiagramTemplate = "MyTemplate1"

arcpy.AddRelativeMainlineLayout_nd(input_Network, input_DiagramTemplate, 
                               "ACTIVE", "LineTrack",
                               "FROM_LEFT_RIGHT", 2, 45)