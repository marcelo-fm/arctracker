# Name: RetrieveAStoredDiagramAndApplyALayoutOnIt.py
# Description:  Retrieve a stored diagram and apply a layout to it.

# Import system modules
import arcpy

# Initialize variables
input_Network = "https://cezembre.esri.com/server/rest/services/Naperville2_Electric_SQL/FeatureServer/0"
input_DiagramName = "my1stdiagram"

# Set overwrite option
arcpy.env.overwriteOutput = True

# Retrieving a given stored diagram and transforming it as a diagram layer 
arcpy.nd.MakeDiagramLayer(input_Network, input_DiagramName, "built_diagramlayer")

# Applying the smart tree layout on this diagram 
arcpy.nd.ApplySmartTreeLayout("built_diagramlayer")