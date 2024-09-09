# Name: Solve_Workflow.py
# Description: Solve a closest facility analysis to find the closest warehouse
#              from the store locations and save the results to a layer file on
#              disk.
# Requirements: Network Analyst Extension

#Import system modules
import arcpy
from arcpy import env
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
    input_gdb = "C:/Data/Paris.gdb"
    network = os.path.join(input_gdb, "Transportation", "ParisMultimodal_ND")
    layer_name = "ClosestWarehouse"
    travel_mode = "Driving Time"
    facilities = os.path.join(input_gdb, "Analysis", "Warehouses")
    incidents = os.path.join(input_gdb, "Analysis", "Stores")
    output_layer_file = os.path.join(output_dir, layer_name + ".lyrx")

    #Create a new closest facility analysis layer.
    result_object = arcpy.na.MakeClosestFacilityAnalysisLayer(network,
                                            layer_name, travel_mode,
                                            "TO_FACILITIES",
                                            number_of_facilities_to_find=1)

    #Get the layer object from the result object. The closest facility layer can
    #now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    #Get the names of all the sublayers within the closest facility layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    #Stores the layer names that we will use later
    facilities_layer_name = sublayer_names["Facilities"]
    incidents_layer_name = sublayer_names["Incidents"]

    #Load the warehouses as Facilities using the default field mappings and
    #search tolerance
    arcpy.na.AddLocations(layer_object, facilities_layer_name,
                            facilities, "", "")

    #Load the stores as Incidents. Map the Name property from the NOM field
    #using field mappings
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                    incidents_layer_name)
    field_mappings["Name"].mappedFieldName = "NOM"
    arcpy.na.AddLocations(layer_object, incidents_layer_name, incidents,
                          field_mappings, "")

    #Solve the closest facility layer
    arcpy.na.Solve(layer_object)

    #Save the solved closest facility layer as a layer file on disk
    layer_object.saveACopy(output_layer_file)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))