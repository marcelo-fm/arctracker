import json

network = r"C:/Data/SanFrancisco.gdb/Transportation/Streets_ND"
# Get all travel modes from the network dataset
travel_modes = arcpy.na.GetTravelModes(network)
# Get the Driving Distance travel mode
dd_travel_mode = travel_modes["Driving Distance"]
# Make a json representation of the travel mode
travel_mode_json = json.loads(str(dd_travel_mode))
# Modify the userHierarchy property to turn hierarchy off, and update the name
travel_mode_json["useHierarchy"] = False
travel_mode_json["name"] = "Driving Distance without Hierarchy"
# Create a new travel mode object from the modified json
new_travel_mode_object = arcpy.na.TravelMode(json.dumps(travel_mode_json))
# Use the new travel mode object to MakeODCostMatrixAnalysisLayer
# We could also pass in the json directly without first converting it to an object
arcpy.na.MakeODCostMatrixAnalysisLayer(network, "OD Without Hierarchy", new_travel_mode_object)