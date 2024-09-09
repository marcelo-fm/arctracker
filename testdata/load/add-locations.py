# Name: AddLocations_Workflow.py
# Description: Calculate a travel time matrix between stores. Use the Add
#               Locations tool to load origins and destinations into an OD Cost
#               Matrix layer. Since the origins and destinations are the same in
#               this case, the origins are first loaded from the stores feature
#               class using geometry, and the destinations are loaded from the
#               origins using network location fields in order to speed up the
#               load times.
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
    layer_name = "StoreTravelTimeMatrix"
    travel_mode = "Driving Time"
    stores = os.path.join(input_gdb, "Analysis", "Stores")
    search_tolerance = "500 Meters"
    search_query = [["Streets", '"FREEWAY" = 0'], ["Streets_ND_Junctions", ""]]
    output_layer_file = os.path.join(output_dir, layer_name + ".lyrx")

    # Create a new OD cost matrix analysis layer. For this scenario, the default
    # value for all the remaining parameters statisfies the analysis requirements
    result_object = arcpy.na.MakeODCostMatrixAnalysisLayer(
        network, layer_name, travel_mode
    )

    # Get the layer object from the result object. The OD cost matrix layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the OD layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    # Store the layer names for later use
    origins_layer_name = sublayer_names["Origins"]
    destinations_layer_name = sublayer_names["Destinations"]

    # Load store features as origins using the geometry of store features.
    # Ensure that the stores are not located on freeways by using a search query.
    arcpy.na.AddLocations(
        layer_object, origins_layer_name, stores, "",
        search_tolerance, search_query=search_query
    )

    # Because we want our origins and destinations to be the same, load the
    # origins as destinations using the network locations fields. Loading using
    # existing network location fields is much faster than loading using geometry
    # because the network locations have already been calculated.
    # Create a field mappings object that supports network location fields using
    # the candidate fields from origins
    origins_sublayer = arcpy.na.GetNASublayer(layer_object, "Origins")
    candidate_fields = arcpy.ListFields(origins_sublayer)
    field_mappings = arcpy.na.NAClassFieldMappings(
        layer_object, destinations_layer_name, True, candidate_fields
    )
    arcpy.na.AddLocations(
        layer_object, destinations_layer_name, origins_sublayer, field_mappings
    )

    # Solve the od cost matrix layer. Halt the execution if there is an
    # invalid location
    arcpy.na.Solve(layer_object, "HALT")

    # Save the solved OD cost matrix layer as a layer file on disk
    layer_object.saveACopy(output_layer_file)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))