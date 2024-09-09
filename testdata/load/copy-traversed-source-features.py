# Name: CopyTraversedSourceFeatures_ex02.py
# Description: The scenario shows how to find the streets that are common to the
#              routes between the closest fire station and the census tract
#              centroids. These streets can be used to identify critical points
#              in case of an emergency.
# Requirements: Network Analyst Extension

# Import system modules
import os
import arcpy
from arcpy import env

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
    env.qualifiedFieldNames = False

    # Set local variables
    input_gdb = "C:/Data/SanFrancisco.gdb"
    output_gdb = "C:/Data/Output.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    layer_name = "EmergencyRoutes"
    travel_mode = "Driving Time"
    facilities = os.path.join(input_gdb, "Analysis", "FireStations")
    incidents = os.path.join(input_gdb, "Analysis", "TractCentroids")
    edge_frequency = os.path.join(output_gdb, "EdgeFrequency")
    critical_streets = os.path.join(output_gdb, "CriticalStreets")

    # Create a new closest facility analysis layer.
    result_object = arcpy.na.MakeClosestFacilityAnalysisLayer(
        network, layer_name, travel_mode, "FROM_FACILITIES"
    )

    # Get the layer object from the result object. The closest facility layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the closest facility layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    # Stores the layer names that we will use later
    facilities_layer_name = sublayer_names["Facilities"]
    incidents_layer_name = sublayer_names["Incidents"]

    # Load fire station features as facilities
    arcpy.na.AddLocations(layer_object, facilities_layer_name, facilities)

    # Load tract centroids as incidents. Map the ID field from Tract
    # Centroids as the name for incidents using field mappings
    field_mappings = arcpy.na.NAClassFieldMappings(
        layer_object, incidents_layer_name
    )
    field_mappings['Name'].mappedFieldName = "ID"
    arcpy.na.AddLocations(
        layer_object, incidents_layer_name, incidents, field_mappings
    )

    # Solve the closest facility layer and copy the travered source features to
    # the output geodatabase. Use default names for the output feature
    # classes and table. Retrieve the first output, which is the traversed edges.
    traversed_edges = arcpy.na.CopyTraversedSourceFeatures(
        layer_object, output_gdb
    ).getOutput(0)

    # Some streets might be traversed by more than one route. Streets traversed
    # by many routes are the most critical emergency routes. Count the number of
    # routes using each street.
    arcpy.analysis.Frequency(
        traversed_edges, edge_frequency, ["SourceOID", "SourceName"]
    )

    # The resulting edge features from CopyTraversedSourceFeatures may include
    # clipped versions of the original street features because the Closest
    # Facility route only traveled across part of the street feature. Select
    # the complete street features from the original street feature class and
    # copy them to output.
    # Get the full path to the network dataset's streets feature class by
    # describing the network dataset.
    network_desc = arcpy.Describe(network)
    edge_sources = network_desc.edgeSources
    for es in edge_sources:
        if es.name.lower() == "streets":
            streets_source = os.path.join(os.path.dirname(network), es.name)
            break

    # Select the relevant streets based on overlap with the results from
    # CopyTraversedSourceFeatures
    streets_layer = arcpy.management.MakeFeatureLayer(
        streets_source, "StreetsLayer"
    )
    arcpy.management.SelectLayerByLocation(
        streets_layer, "SHARE_A_LINE_SEGMENT_WITH", traversed_edges
    )

    # Add the frequency information to the output feature class using JoinField
    arcpy.management.JoinField(
        streets_layer, "ObjectID", edge_frequency, "SourceOID", "FREQUENCY"
    )

    # Save the selected features to disk
    arcpy.management.CopyFeatures(streets_layer, critical_streets)

    # Delete the Frequency field from the street feature class
    arcpy.management.DeleteField(streets_layer, "FREQUENCY")

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))