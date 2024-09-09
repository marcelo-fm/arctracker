# Name: ShareAsRouteLayers_Workflow.py
# Description: Find the closest warehouse from the store locations and share the
#              results as route layers.
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

    # Check if logged into active Portal. Fail if not logged into actiave portal.
    if arcpy.GetSigininToken() is None:
        raise arcpy.ExecuteError("Please sign in to your active portal in ArcGIS Pro.")
    
    # Set environment settings
    output_dir = "C:/Data"
    # The NA layer's data will be saved to the workspace specified here
    env.workspace = os.path.join(output_dir, "Output.gdb")
    env.overwriteOutput = True

    # Set local variables
    input_gdb = "C:/Data/Paris.gdb"
    network = os.path.join(input_gdb, "Transportation", "ParisMultimodal_ND")
    layer_name = "ClosestWarehouse"
    travel_mode = "Driving Time"
    facilities = os.path.join(input_gdb, "Analysis", "Warehouses")
    incidents = os.path.join(input_gdb, "Analysis", "Stores")

    # Create a new closest facility analysis layer. 
    result_object = arcpy.na.MakeClosestFacilityAnalysisLayer(network,
                                    layer_name, travel_mode, "TO_FACILITIES",
                                    number_of_facilities_to_find=1)

    # Get the layer object from the result object. The closest facility layer can
    # now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    # Get the names of all the sublayers within the closest facility layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    # Stores the layer names that we will use later
    facilities_layer_name = sublayer_names["Facilities"]
    incidents_layer_name = sublayer_names["Incidents"]

    # Load the warehouses as Facilities using the default field mappings and
    # search tolerance
    arcpy.na.AddLocations(layer_object, facilities_layer_name,
                            facilities, "", "")

    # Load the stores as Incidents. Map the Name property from the NOM field
    # using field mappings
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                    incidents_layer_name)
    field_mappings["Name"].mappedFieldName = "NOM"
    arcpy.na.AddLocations(layer_object, incidents_layer_name, incidents,
                          field_mappings, "")

    # Solve the closest facility layer
    arcpy.na.Solve(layer_object)

    # Share the routes from the closest facility analysis as route layers
    arcpy.na.ShareAsRouteLayers(layer_object, "Share closest facility solve result as route layers")

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))