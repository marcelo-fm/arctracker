import arcpy
input_Network = "https://cezembre.esri.com/server/rest/services/Naperville_Electric_SQL/FeatureServer/0"
arcpy.DeleteDiagram_nd(input_Network, "ReducedDiagrams")