import arcpy
import os

input_SourceNetwork = "D:/MyProjectLocation/MyDatabaseSourceConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
input_DestinationNetwork = "D:/MyProjectLocation/MyDatabaseDestinationConnection.sde/MyDatabase.MAP.Electric/MyDatabase.MAP.Electric"
folder = "D:/MyProjectLocation/"
input_SourceTemplate = "SourceTemplate"
input_DestinationTemplate = "DestinationTemplate"

arcpy.nd.ExportDiagramTemplateDefinitions(input_SourceNetwork, 
                                          input_SourceTemplate, 
                                          os.path.join(folder, "DiagramRuleAndLayoutDefinitions.ndbd"), 
                                          os.path.join(folder, "DiagramLayerDefinition.ndld"))
arcpy.nd.ImportDiagramTemplateDefinitions(input_DestinationNetwork, 
                                          input_DestinationTemplate, 
                                          os.path.join(folder, "DiagramRuleAndLayoutDefinitions.ndbd"),
                                          os.path.join(folder, "DiagramLayerDefinition.ndld"))