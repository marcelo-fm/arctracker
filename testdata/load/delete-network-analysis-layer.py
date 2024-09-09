import arcpy
layer = arcpy.na.MakeVehicleRoutingProblemAnalysisLayer(network, "VRP").getOutput(0)

# Additional workflow steps

arcpy.na.DeleteNetworkAnalysisLayer(layer)