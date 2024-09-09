# Name: Directions_Workflow.py
# Description: Generate driving directions in an html file for a route that
#              visits the store locations in the best sequence in order to
#              minimize the total travel time
# Requirements: Network Analyst Extension

# Import system modules
import arcpy
from arcpy import env
import os

try:
    # Check out Network Analyst license if available. Fail if the Network Analyst license is not available.
    if arcpy.CheckExtension("network") == "Available":
        arcpy.CheckOutExtension("network")
    else:
        raise arcpy.ExecuteError("Network Analyst Extension license is not available.")

    # Set environment settings
    output_dir = "C:/Data"
    # The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    # Set inputs and outputs
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    layer_name = "StoreRoute"
    travel_mode = "Driving Time"
    start_location = os.path.join(input_gdb, "Analysis", "DistributionCenter")
    store_locations = os.path.join(input_gdb, "Analysis", "Stores")
    output_directions = os.path.join(
        output_dir, layer_name + "_Directions.html")
    output_layer_file = os.path.join(output_dir, layer_name + ".lyrx")

    # Create a new route layer. The route starts at the distribution center and
    # visits the stores in the best order to yield the shortest travel time.
    result_object = arcpy.na.MakeRouteAnalysisLayer(
        network, layer_name, travel_mode, "PRESERVE_FIRST", time_of_day="8:00 AM"
    )

    # Get the layer object from the result object. The route layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the route layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    #Stores the layer names that we will use later
    stops_layer_name = sublayer_names["Stops"]

    # Load the distribution center as the start location using default field
    # mappings and search tolerance
    arcpy.na.AddLocations(
        layer_object, stops_layer_name, start_location, "", ""
    )

    # Load the store locations as stops. Make sure the store locations are
    # appended to the Stops sublayer so the distribution center you just loaded
    # isn't overwritten. Map the ServiceTime field from the input data to the
    # Attr_[impedance] property in the Stops sublayer so that the time it takes to
    # service each store is included in the total travel time for the route.
    # Figure out what the impedance attrbute is
    solver_props = arcpy.na.GetSolverProperties(layer_object)
    impedance = solver_props.impedance
    # Handle field mappings
    field_mappings = arcpy.na.NAClassFieldMappings(
        layer_object, stops_layer_name
    )
    field_mappings["Name"].mappedFieldName = "Name"
    field_mappings["Attr_" + impedance].mappedFieldName = "ServiceTime"
    arcpy.na.AddLocations(
        layer_object, stops_layer_name, store_locations,
        field_mappings, "", append="APPEND"
    )

    # Generate driving directions in an HTML file
    arcpy.na.Directions(
        layer_object, "HTML", output_directions, "Miles",
        "REPORT_TIME", impedance
    )

    # Save the solved na layer as a layer file on disk
    layer_object.saveACopy(output_layer_file)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))