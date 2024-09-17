# Name: AlterDiagramProperties.py
# Description:  Retrieve a stored diagram and change its properties.

# Import system modules
import arcpy

# Initialize variables
input_network = "https://cezembre.esri.com/server/rest/services/Naperville_ORA/FeatureServer/8"
input_DiagramName = "Test"

# Set overwrite option
arcpy.env.overwriteOutput = True

# Retrieving a given stored diagram and transforming it as a diagram layer 
arcpy.MakeDiagramLayer_nd(input_network, input_DiagramName, "built_diagramlayer")

# Renaming this diagram to "SmartTree1_Test", changing its access right 
# level, and specifying tags 
arcpy.AlterDiagramProperties_nd("built_diagramlayer", "SmartTree1_Test", 
                                "PROTECTED", 
                                "Distribution#RMT0003#Naperville North East")