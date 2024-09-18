# Name: GenerateAndStoreADiagram.py
# Description:  Generate and store a diagram from a set of features based on a feature class and an attribute query.

# Import system modules
import arcpy

# Initialize variables
input_network = "https://cezembre.esri.com/server/rest/services/Naperville_Electric_SQL/FeatureServer/0"
input_fc = "https://cezembre.esri.com/server/rest/services/Naperville_Electric_SQL/FeatureServer/7"
sql_expression = "SUBNETWORKNAME='RMT003'"
template_name = "Basic"
output_diagram_name = "MyBasicRMT003Diagram"

# Set overwrite option
arcpy.env.overwriteOutput = True

# Make a layer from features in the feature class filtered out using an attribute query
FeatureLayer = arcpy.management.MakeFeatureLayer(input_fc, "built_featurelayer", 
                                                 sql_expression)

# Create a diagram based on a given template name from those features
result = arcpy.nd.CreateDiagram(input_network, template_name, 
                                "built_featurelayer")
diagram_name = result[1]
arcpy.nd.MakeDiagramLayer(input_network, diagram_name, 
                          "built_diagramlayer")

# Store the resulting diagram in the database. 
arcpy.nd.StoreDiagram("built_diagramlayer", output_diagram_name)