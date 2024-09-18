import arcpy

input_Network = "https://cezembre.esri.com/server/rest/services/Naperville2_Electric_SQL/FeatureServer/0"
input_TemplateName = "Basic"
arcpy.nd.UpdateDiagram(input_Network, input_TemplateName)