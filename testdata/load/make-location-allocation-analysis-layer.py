# Name: MakeLocationAllocationAnalysisLayer_Workflow.py
# Description: Choose the store locations that would generate the most business
#              for a retail chain. For this scenario, we will perform the
#              location-Allocation analysis using the maximize attendance
#              problem type.
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
    input_gdb = "C:/Data/SanFrancisco.gdb"
    network = os.path.join(input_gdb, "Transportation", "Streets_ND")
    layer_name = "NewStoreLocations"
    travel_mode = "Driving Time"
    facilities = os.path.join(input_gdb, "Analysis", "CandidateStores")
    required_facility = os.path.join(input_gdb, "Analysis", "ExistingStore")
    demand_points = os.path.join(input_gdb, "Analysis", "TractCentroids")
    output_layer_file = os.path.join(output_dir, layer_name + ".lyrx")

    #Create a new location-allocation layer. In this case, the demand travels to
    #the facility. We wish to find 3 potential store locations out of all the
    #candidate store locations using the maximize attendance model.
    result_object = arcpy.na.MakeLocationAllocationAnalysisLayer(network,
                                    layer_name, travel_mode, "TO_FACILITIES",
                                    "MAXIMIZE_ATTENDANCE", cutoff=20,
                                    number_of_facilities_to_find=3)

    #Get the layer object from the result object. The location-allocation layer
    #can now be referenced using the layer object.
    layer_object = result_object.getOutput(0)

    #Get the names of all the sublayers within the location-allocation layer.
    sublayer_names = arcpy.na.GetNAClassNames(layer_object)
    #Stores the layer names that we will use later
    facilities_layer_name = sublayer_names["Facilities"]
    demand_points_layer_name = sublayer_names["DemandPoints"]

    #Load the candidate store locations as facilities using default search
    #tolerance and field mappings.
    arcpy.na.AddLocations(layer_object, facilities_layer_name, facilities, "",
                                                                            "")

    #Load the existing store location as the required facility. Use the field
    #mappings to set the facility type to requried. We need to append this
    #required facility to existing facilities.
    field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                    facilities_layer_name)
    field_mappings["FacilityType"].defaultValue = 1
    arcpy.na.AddLocations(layer_object, facilities_layer_name,
                            required_facility, field_mappings, "",
                            append="APPEND")

    #Load the tract centroids as demand points using default search tolerance
    #Use the field mappings to map the Weight property from POP2000 field.
    demand_field_mappings = arcpy.na.NAClassFieldMappings(layer_object,
                                                    demand_points_layer_name)
    demand_field_mappings["Weight"].mappedFieldName = "POP2000"
    arcpy.na.AddLocations(layer_object, demand_points_layer_name, demand_points,
                          demand_field_mappings, "")

    #Solve the location-allocation layer
    arcpy.na.Solve(layer_object)

    #Save the solved location-allocation layer as a layer file on disk
    layer_object.saveACopy(output_layer_file)

    print("Script completed successfully")

except Exception as e:
    # If an error occurred, print line number and error message
    import traceback, sys
    tb = sys.exc_info()[2]
    print("An error occurred on line %i" % tb.tb_lineno)
    print(str(e))