import arcpy
source_Network = "D:/MyProjectLocation/MyDatabaseSourceConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
arcpy.nd.ChangeDiagramsOwner(
    source_Network, "userB", "", 
    ["Diagram78951", "Diagram78952", "Diagram78967", "Diagram25789"])