# Name: MakeRouteAnalysisLayer_MultiRouteWorkflow.py
# Description: Calculate the home-work commutes for a set of people and save
#              the output to a feature class
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env
import datetime
import os

try:
    #Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")
    
    #Set environment settings
    output_dir = "C:/Data"
    #The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    #Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    stops_home = os.path.join(input_gdb, "Analysis", "Commuters_Home")
    stops_work = os.path.join(input_gdb, "Analysis", "Commuters_Work")
    layer_name = "Commuters"
    out_routes_featureclass = "Commuter_Routes"
    travel_mode = "Driving Time"

    #Set the time of day for the analysis to 8AM on a generic Monday.
    start_time = datetime.datetime(1900, 1, 1, 8, 0, 0)

    #Create a new Route layer.  Optimize on driving time, but compute the
    #distance traveled by accumulating the Meters attribute.
    result_object = arcpy.na.MakeRouteAnalysisLayer(network, layer_name,
                                        travel_mode, time_of_day=start_time,
                                        accumulate_attributes=["Meters"])

    #Get the layer object from the result object. The route layer can now be
    #referenced using the layer object.
    layer_object = result_object.getOutput(0)

    #Get the names of all the sublayers within the route layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    #Stores the layer names that we will use later
    stops_layer_name = sublayer_names["Stops"]
    routes_layer_name = sublayer_names["Routes"]

    #Before loading the commuters' home and work locations as route stops, set
    #up field mapping.  Map the "Commuter_Name" field from the input data to
    #the RouteName property in the Stops sublayer, which ensures that each
    #unique Commuter_Name will be placed in a separate route.  Matching
    #Commuter_Names from stops_home and stops_work will end up in the same
    #route.
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object, stops_layer_name)
    field_mappings["RouteName"].mappedFieldName = "Commuter_Name"

    #Add the commuters' home and work locations as Stops. The same field mapping
    #works for both input feature classes because they both have a field called
    #"Commuter_Name"
    arcpy.na.AddLocations(layer_object, stops_layer_name, stops_home,
                        field_mappings, "")
    arcpy.na.AddLocations(layer_object, stops_layer_name, stops_work,
                        field_mappings, "", append="APPEND")

    #Solve the route layer.
    arcpy.na.Solve(layer_object)

    # Get the output Routes sublayer and save it to a feature class
    routes_sublayer = arcpy.na.GetNASublayer(layer_object, "Routes")
    arcpy.management.CopyFeatures(routes_sublayer, out_routes_featureclass)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))