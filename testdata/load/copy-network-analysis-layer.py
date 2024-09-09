import arcpy

# Retrieve the existing network analysis layer named "Route" from the map
project = arcpy.mp.ArcGISProject("CURRENT")
map_object = project.listMaps()[0]
route_layer = map_object.listLayers("Route")[0]

# Copy the existing layer to a new layer
copied_route_layer = arcpy.na.CopyNetworkAnalysisLayer(route_layer, "Copied Route").getOutput(0)

# Perform further analysis as desired
arcpy.na.Solve(copied_route_layer)